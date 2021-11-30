from django.shortcuts import render
from django.shortcuts import redirect

TASKS = []

# Create your views here.
def register(request):
    return render(
        request,
        'form_app3/register.html'
    )

def tasks_list(request):
    if request.method == "POST":
        task = request.POST.get('task')
        if task:
            TASKS.append(task)

        return redirect('form_app3:tasks-list')


    return render(
        request,
        'form_app3/tasks_list.html',
        context={
            'tasks': TASKS
        }
    )
