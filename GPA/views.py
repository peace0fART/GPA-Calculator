# GPA views

from django.http import HttpResponse
from django.shortcuts import render, redirect

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')

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