from django.urls import path
from new import views

app_name = 'new'

urlpatterns = [
    path('', views.new, name=""),
    path('home', views.home, name="home")
]
