from django.urls import path
from links import views

app_name = 'links'

urlpatterns = [
    path('first/', views.first, name="first"),
    path('second/', views.second, name='second'),  # nazwy mapowań
    path('third/<str:value>', views.third, name='third'),  # nazwy mapowań
]
