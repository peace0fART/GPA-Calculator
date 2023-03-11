from django.contrib import admin
from django.urls import path, include
from . import views

# sgpa urls
urlpatterns = [
    path('', views.sgpa_home, name="sgpa_home"),
    path('sem01', views.sem_01, name="sem_01"),
    path('sem02', views.sem_02, name="sem_02"),
    path('sem03', views.sem_03, name="sem_03"),
    path('sem04', views.sem_04, name="sem_04"),
    path('sem05', views.sem_05, name="sem_05"),
    path('sem06', views.sem_06, name="sem_06"),
    path('sem07', views.sem_07, name="sem_07"),
    path('sem08', views.sem_08, name="sem_08"),
    path('home', views.go_home, name='go_home'),
    path('about', views.go_about, name='go_about'),
    path('contact', views.go_contact, name='go_contact'),
    path('sgpa_home', views.go_sgpa, name='go_sgpa'),
    path('cgpa', views.go_sgpa, name='go_cgpa'),
    ]