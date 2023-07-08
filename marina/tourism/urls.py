from django.urls import path
from . import views

urlpatterns = [
path('bandb/', views.hotel, name='b&b'),
]