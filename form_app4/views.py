from django.shortcuts import render
from django.shortcuts import redirect

# TASKS = []

# Create your views here.
def register(request):
    return render(
        request,
        'form_app4/register.html'
    )


def tasks_list(request):
    with open('tasks.txt', 'a+') as f:  # otworzenie pliku (zastąpienie linijki powyżej)
        if request.method == "POST":
            task = request.POST.get('task')
            if task:
                # TASKS.append(task)  #dodanie do listy
                f.write(task + "\n")

            return redirect('form_app4:tasks-list') #przekierowanie

    with open('tasks.txt', 'r') as f:
        tasks = f.readlines()

    return render(
        request,
        'form_app4/tasks_list.html',
        context={
            'tasks': tasks#TASKS  # przekazanie listy do szablonu
        }
    )
