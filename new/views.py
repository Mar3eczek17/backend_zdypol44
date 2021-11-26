from django.shortcuts import render

# Create your views here.
def new(request):
    return render(
        request,
        'layout.html'
    )

def home(request):
    return render(
        request,
        'home/children.html'
    )