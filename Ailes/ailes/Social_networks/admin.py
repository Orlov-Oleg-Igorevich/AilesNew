from django.contrib import admin
from .models import PersonInfo

# Register your models here.
@admin.register(PersonInfo)
class PersonInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'firstname', 'lastname', 'slug')
    list_display_links = ('id', 'firstname')
    readonly_fields = ('friends', 'subscribers', 'subscribes', 'slug')
    list_filter = ('country', 'date_of_birth')
    list_per_page = 5
    ordering = ('id', )
