from django.urls import path
from links import views

urlpatterns = [
    path('mowa/', views.first, name="first"),
    path('abc/', views.second, name='second'),  # nazwy mapowań
]
