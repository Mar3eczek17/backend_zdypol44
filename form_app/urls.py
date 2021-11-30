from django.urls import path

from form_app import views

app_name = 'form_app'

urlpatterns = [
    path('register/', views.register, name='register')
]