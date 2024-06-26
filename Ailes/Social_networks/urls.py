from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='main-page'),
    path("about/", views.about, name='about'),
    path("contact/", views.contact, name='contact'),
    path("news/", views.news, name='News'),
    path("signup/", views.signup, name='signup'),
    path('user/<slug:user_slug>/', views.show_user, name='user'),
    path('user/<slug:user_slug>/friends/', views.user_friends, name='user_friends'),
]
