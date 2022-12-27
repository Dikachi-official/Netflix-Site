"""netflixprj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings        #THE NECSSARY IMPORTS FOR MEDIA FILE LOCATING BELOW
from django.conf.urls.static import static   #THE NECSSARY IMPORTS FOR MEDIA FILE LOCATING BELOW

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include ('netflixapp.urls')),
    path('accounts/', include('allauth.urls')), #THIS PARTICULAR ONE IS NECESSARY FOR ALLAUTH AUTHENTICATION   
                                                #ENSURE YOU "PIP INSTALL DJANGO-ALLAUTH"
]

if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)   #TO LOCATE OUR MEDIA FILES WHICH ARE UPLOADED THROUGH DB
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    #TO BE PASS IN OUR HTML TEMPLATE TO BE DISPLAYED IN FRONTEND
