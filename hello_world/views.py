from django.shortcuts import render
from datetime import datetime

# Create your views here.
def hello(request, name):
    return render(
        request,
        'hello_world/hello.html',
        context={
            'username': name,
        }
    )