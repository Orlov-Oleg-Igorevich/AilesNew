from django.db import models
from django.urls import reverse

class PersonInfo(models.Model):
    firstname = models.CharField(max_length=100, verbose_name='Имя')
    lastname = models.CharField(max_length=100, verbose_name='Фамилия')
    country = models.CharField(max_length=60, default='Russia')
    language = models.CharField(max_length=50, default='Russian')
    date_of_birth = models.DateField()
    time_update = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True, max_length=255, verbose_name='Слаг')
    photo = models.ImageField(width_field=1920, height_field=1080, blank=True)
    occupation = models.CharField(max_length=100, blank=True)
    photos = models.ManyToManyField('PersonPhotos', related_name='user')
    subscribers = models.IntegerField(default=0)
    friends = models.IntegerField(default=0)
    descrip = models.TextField(blank=0, default='Привет! Я использую Ailes!')
    subscribes = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('page', kwargs = {'post_slug': self.slug})

    def __str__(self):
        return self.firstname + self.lastname

    class Meta:
        verbose_name = 'Информация о аккаунте'
        verbose_name_plural = 'Информация о аккаунтах'


class PersonPhotos(models.Model):
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.pk
