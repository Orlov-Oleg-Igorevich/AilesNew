from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='main-page'),
    path("about/", views.about, name='about'),
    path("contact/", views.contact, name='contact'),
    path("News/", views.News, name='News'),
    path("signup/", views.signup, name='signup')
]