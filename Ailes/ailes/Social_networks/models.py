from django.db import models
from django.urls import reverse

class Accounts(models.Model):
    login = models.CharField(unique=True, max_length=60, db_index=True)
    password = models.CharField(max_length=50)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

class PersonInfo(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    country = models.CharField(max_length=60, default='Russia')
    language = models.CharField(max_length=50, default='Russian')
    date_of_birth = models.DateField()
    time_update = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True, max_length=255)
    photo = models.ImageField(width_field=1920, height_field=1080, blank=True)
    acc = models.OneToOneField('Accounts', on_delete=models.CASCADE, related_name='accounts')

    def get_absolute_url(self):
        return reverse('page', kwargs = {'post_slug': self.slug})

    def __str__(self):
        return self.firstname + self.lastname
