from django.shortcuts import render


# Create your views here.

def home (request):
    return render (request, 'farohp.html')

def turismo (request):
    return render (request, 'turismo.html')