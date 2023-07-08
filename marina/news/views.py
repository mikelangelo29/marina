from django.shortcuts import render
from .models import News

# Create your views here.

def news (request):
    notizie=News.objects.all()
    return render(request, "news.html",{'notizie':notizie})