from django.urls import path

from isitchristmas import views

urlpatterns = [
    path('', views.index)
]