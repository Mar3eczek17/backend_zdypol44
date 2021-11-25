from django.urls import path
from links import views

urlpatterns = [
    path('first/', views.first),
    path('second/', views.second),
]