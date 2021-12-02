from django.urls import path
from hello_world import views

urlpatterns = [
    path('hello/<str:name>', views.hello)
]