"""django_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url
from myrestapi import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url('hello/', views.HelloWorld.as_view()),
    url('postcall/', views.Mypostcall.as_view()),
    # url('putcall/', views.Myputcall.as_view())
    url(r'^putcall/(?P<myId>[0-9A-Za-z]+)/?$', views.Myputcall.as_view()),
    url(r'^delcall/(?P<myId>[0-9A-Za-z]+)/?$', views.Mydeletecall.as_view())
]
