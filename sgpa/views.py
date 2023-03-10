# sgpa views

from django.http import HttpResponse
from django.shortcuts import render, redirect

def sgpa_home(request):
    return render(request, 'sgpa/sgpa.html')

def sem_01(request):
    return render(request, 'sgpa/sem01.html')

def go_home(request):
    return redirect('/')

def go_about(request):
    return redirect('/about')

def go_contact(request):
    return redirect('/contact')

def go_sgpa(request):
    return redirect('/sgpa_home')

def go_cgpa(request):
    return redirect('/cgpa')