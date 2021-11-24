from django.urls import path
from isitmonday import views

urlpatterns = [
    path('', views.index)
]