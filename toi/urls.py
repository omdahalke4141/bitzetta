"""
URL configuration for tech_ocean_institute project.

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
from .views import *
from . import views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin_home'),  # Ensure this is unique
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('course_single/', course_single, name='course_single'),
    path('courses/', courses, name='courses'),
    path('notice_single/', notice_single, name='notice_single'),
    path('notice/', notice, name='notice'),
    path('teacher_single/', teacher_single, name='teacher_single'),
    path('teacher/', teacher, name='teacher'),
    path('admin_signin/', admin_signin, name='admin_signin'),
    path('apply_course/', apply_course, name='apply_course'),
     path('', views.home, name='home'),  # Assuming 'home' is your view function for the homepage
]
