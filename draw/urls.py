from django.urls import path
from draw import views

urlpatterns = [
    path('toto-lotek/', views.toto_lotek_view)
]