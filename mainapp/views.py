from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'mainapp/index.html')

def contact(request):
    return render(request, 'mainapp/contact.html')

def doctors(request):
    return render(request, 'mainapp/doctors.html')

def services(request):
    return render(request, 'mainapp/services.html')

def skidki(request):
    return render(request, 'mainapp/skidki.html')
