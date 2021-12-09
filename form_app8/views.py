from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from .models import Task


# Create your views here.
def register(request):  # Create
    if request.method == "POST":
        task = Task()
        task.name = request.POST("task_name")
        task.salary = request.POST("task_salary")
        task.save()
        return redirect('form_app8/register.html')



    # task = request.POST.get('task_name')
    # if task:
    #     Task.objects.create(text=task)
    #     return redirect('form_app8:tasks-list')
    # return render(
    #     request,
    #     'form_app8/register.html',
    # )

def tasks_list(request):  # Read

    tasks = Task.objects.all()

    return render(
        request,
        'form_app8/tasks-list.html',
        context={
            'tasks': tasks,
        }
    )

def update(request, task_id):  # Update
    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":
        update_task = request.POST.get('task')
        if update_task:
            task.text = update_task
            task.save()

        return redirect('form_app8:tasks-list')

    return render(
        request,
        'form_app8/update.html',
        context={
            'task': task,
        }
    )
