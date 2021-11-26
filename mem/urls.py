from django.urls import path
from mem import views

urlpatterns = [
    path('sample', views.sample)
]
