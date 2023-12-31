"""
URL configuration for marina project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from faro import views 
from django.conf.urls.static import static
from django.conf import settings




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='homepage' ),
    path('turismo/', views.turismo, name='turismo'),
    path('tourism/', include('tourism.urls')), 
    path('news/', include ('news.urls')),
    path('search/', views.search, name='cerca'),
    path('storia/', views.storia, name='storia'),
    path('bonifica/', views.storia1, name='stornara'),
    path('insediamenti/', views.storia2, name='insediamenti'),
    path('personaggi/', include ('personaggi.urls')),
    path('biblio/', views.biblio, name='biblio'),
    path('natura/', include('natura.urls')),
    path('50_60/', include('cinquanta.urls')),
    path('chi_siamo/', views.chisiamo, name='chisiamo'),
    
] + static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
