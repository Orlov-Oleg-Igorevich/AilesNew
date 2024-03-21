from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='home'),
    path("News/", views.News, name='news'),
    path("contact/", views.contact, name='contact'),
    path("about/", views.about, name='about'),
    path("signup/", views.signup, name='signup')
]