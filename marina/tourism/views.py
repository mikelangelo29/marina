from django.shortcuts import render
from .models import Hotel


def hotel (request):
    ostelli=Hotel.objects.all()
    return render(request, "alberghi.html",{'ostelli':ostelli})


