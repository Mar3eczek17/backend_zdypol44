from django.urls import path

from hello import views

urlpatterns = [
    path('home/', views.hello),
    path('home2/', views.hello2),
]
