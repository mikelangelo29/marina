
from django.urls import path
from . import views

urlpatterns = [
path('notizie/', views.news, name='notizie'),
]