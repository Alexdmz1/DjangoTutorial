from django.shortcuts import render




def home(request):
    return render(request, 'home.html',{})

def herencia(request):
    return render(request, 'herencia.html')

def otra(request):
    return render(request, 'otra.html')

def ejemplo(request):
    return render(request, 'ejemplo.html')

def index(request):
    return render(request, 'index.html')
