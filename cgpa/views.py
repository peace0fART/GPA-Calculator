from django.shortcuts import render, redirect

# cgpa views
# Create your views here.
def cgpa(request):
    return render(request, 'cgpa/cgpa.html')

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