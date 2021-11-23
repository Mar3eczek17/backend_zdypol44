from django.urls import path

from hello import views

urlpatterns = [
    path('home/', views.hello_view),
    path('home2/', views.hello2_view),
    path('adam/', views.adam_view),
    path('ewa/', views.ewa_view),
    # path('<str:name>/', views.name_view),  #Konwerter ścieżki
    path('<str:name>', views.name_view2),
]
