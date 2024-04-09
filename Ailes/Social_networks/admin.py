from django.contrib import admin
from .models import PersonInfo
from django.utils.safestring import mark_safe


# Register your models here.
@admin.register(PersonInfo)
class PersonInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'firstname', 'lastname', 'slug', 'show_photo', 'show_profile_hat')
    list_display_links = ('id', 'firstname')
    readonly_fields = ('friends', 'subscribers', 'show_photo', 'show_profile_hat', 'subscribes', 'slug')
    list_filter = ('country', 'date_of_birth')
    fields = ['firstname', 'lastname', 'slug', 'show_photo', 'date_of_birth', 'photo', 'profile_hat', 'show_profile_hat']
    list_per_page = 5
    ordering = ('id', )

    @admin.display(description='Фото')
    def show_photo(self, person: PersonInfo):
        if person.photo:
            return mark_safe(f"<img src='{person.photo.url}' width=50>")

    @admin.display(description='Шапка профиля')
    def show_profile_hat(self, person: PersonInfo):
        if person.profile_hat:
            return mark_safe(f"<img src='{person.profile_hat.url}' width=50>")

