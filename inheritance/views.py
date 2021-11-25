from django.shortcuts import render

# Create your views here.
def first(request):
    return render(
        request,
        'inheritance/first.html'
    )


def second(request):
    return render(
        request,
        'inheritance/second.html'
    )