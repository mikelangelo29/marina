from django.shortcuts import render
from .models import Hotel, Risto

def hotel (request):
    ostelli=Hotel.objects.all()
    return render(request, "alberghi.html",{'ostelli':ostelli})

def risto (request):
    pubs=Risto.objects.all()
    return render(request, "pubs.html",{'pubs':pubs})


