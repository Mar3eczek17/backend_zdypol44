from django.urls import path

from form_app2 import views

app_name = 'form_app2'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('tasks-list/', views.tasks_list, name='tasks-list'),
]