"""djangoGirl URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib.auth import login
from django.urls import path, include
from blog import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('admin/', admin.site.urls, name='admin'),
    path('blog/', include(('blog.urls', 'blog'), namespace='blog')),
    path('signup/', views.signuppage, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),

]
