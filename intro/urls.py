"""intro URL Configuration

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
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', include('hello.urls')),
    path('isitchristmas/', include('isitchristmas.urls')),
    path('fruits/', include('fruits.urls')),
    path('isitmonday/', include('isitmonday.urls')),
    path('draw/', include('draw.urls')),
    path('links/', include('links.urls')),
    path('inheritance/', include('inheritance.urls')),
    path('mem/', include('mem.urls')),
    path('new/', include('new.urls')),
    path('form_app/', include('form_app.urls')),
    path('form_app2/', include('form_app2.urls')),
    path('form_app3/', include('form_app3.urls')),
    path('form_app4/', include('form_app4.urls')),
    path('form_app5/', include('form_app5.urls')),
    path('hello_world/', include('hello_world.urls')),
    path('form_app6/', include('form_app6.urls')),
    path('form_app7/', include('form_app7.urls')),
    path('crud/', include('crud.urls')),
    path('form_app8/', include('form_app8.urls')),
]
