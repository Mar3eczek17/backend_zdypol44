from django.shortcuts import render, redirect
from .models import Employee
# Create your views here.
def index(request):
    return render(request, 'crud/index.html')

def base(request):
    return render(request, 'crud/base.html')

def add_new_employee(request):
    if request.method == "POST":
        employee = Employee()
        employee.name = request.POST["employee_name"]
        employee.salary = request.POST["employee_salary"]
        employee.save()
        return redirect('crud:index')

def show_all_employees(request):
    employees = Employee.objects.all()
    return render(
        request,
        'crud/show_all_employees.html',
        context={
            'employees': employees
        }
    )

def edit_employee(request, id):
    id = int(id)
    emp = Employee.objects.get(pk=id)
    if request.method == "GET":
        context = {
            "employee": emp
        }
        return render(request, "crud/edit_employee.html", context)

def edit_employee_save(request):
    if request.method == "POST":
        id = request.POST["employee_id"]
        id = int(id)
        e = Employee.objects.get(pk=id)
        e.name = request.POST["employee_name"]
        e.salary = request.POST["employee_salary"]
        e.save()

        return redirect('crud:show_all_employees')

def delete_employee(request, id):
    if request.method == "GET":
        id = int(id)
        e = Employee.objects.get(pk=id)
        e.delete()

        return redirect("crud:show_all_employees")



