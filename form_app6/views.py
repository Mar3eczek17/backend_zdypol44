from django.http import Http404
from django.shortcuts import render

from form_app6.models import Task
from django.shortcuts import redirect
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404


# Create your views here.
def register(request):
    # print(dir(request)) - request potrafi wiele rzeczy
    task = request.POST.get('task')  # post w ciele, get w adresie
    if task:
        Task.objects.create(text=task)

        return redirect('form_app6:tasks-list')

    return render(
        request,
        'form_app6/register.html',
    )

def tasks_list(request):

    tasks = Task.objects.all() #wczytuje wszystkie zadania

    return render(
        request,
        'form_app6/tasks-list.html',
        context={
            'tasks': tasks, # przekazuje do szablonu i wyswietla
        }
    )

def update(request, task_id):
    # try:
    #     task = Task.objects.get(id=task_id)
    # except ObjectDoesNotExist:
    #     raise Http404()

    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":
        updated_task = request.POST.get('task')
        if updated_task:
            task.text = updated_task
            task.save()

        return redirect('form_app6:tasks-list')

    return render(
        request,
        'form_app6/update.html',
        context={
            'task': task,
        }
    )

# krok3 trzeba wyciagnac task
def delete(request, task_id):

        if request.method == "POST": # Z PALCA SIE NIE DA, BEZ TEJ KOMENTY MOZNA USUNAC ZE SCIEZKI
            task = get_object_or_404(Task, id=task_id) #wczytuje wszystkie zadania
            task.delete()

        return redirect('form_app6:tasks-list')