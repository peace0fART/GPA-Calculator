# sgpa views

from django.http import HttpResponse
from django.shortcuts import render, redirect

def sgpa_home(request):
    return render(request, 'sgpa/sgpa.html')

def sem_01(request):
    return render(request, 'sgpa/sem01.html')

def sem_02(request):
    return render(request, 'sgpa/sem02.html')

def sem_03(request):
    return render(request, 'sgpa/sem03.html')

def sem_04(request):
    return render(request, 'sgpa/sem04.html')

def sem_05(request):
    return render(request, 'sgpa/sem05.html')

def sem_06(request):
    return render(request, 'sgpa/sem06.html')

def sem_07(request):
    return render(request, 'sgpa/sem07.html')

def sem_08(request):
    return render(request, 'sgpa/sem08.html')

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