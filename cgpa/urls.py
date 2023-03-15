from django.urls import path, include
from . import views

#cgpa usrls
urlpatterns = [
    path('', views.cgpa, name='cgpa'),
    path('home', views.go_home, name='go_home'),
    path('about', views.go_about, name='go_about'),
    path('contact', views.go_contact, name='go_contact'),
    path('sgpa_home', views.go_sgpa, name='go_sgpa'),
    path('cgpa', views.go_cgpa, name='go_cgpa'),
]