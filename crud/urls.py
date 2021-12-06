from django.urls import path, include
from . import views

app_name = 'crud'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('base/', views.base, name='base'),
    path('add_new_employee/', views.add_new_employee, name='add_new_employee'),
    path('show_all_employees/', views.show_all_employees, name='show_all_employees'),
    path('edit_employee/<str:id>/', views.edit_employee, name='edit_employee'),
    path('edit_employee_save/', views.edit_employee_save, name='edit_employee_save'),
    path('delete_employee/<str:id>/', views.delete_employee, name='delete_employee'),
]
