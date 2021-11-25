from django.urls import path

from inheritance import views

app_name = 'inheritance'

urlpatterns = [
    path('first/', views.first, name='first'),
    path('second/', views.second, name='second')
]
