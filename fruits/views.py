from django.shortcuts import render

# Create your views here.
def index(request):

    fruits = [
        'ananas',
        'cytryna',
        'pomarnacza',
        'jablko',
    ]

    return render(
        request,
        'fruits/index.html',
        context={
            'fruits': fruits,  # Zmienne kontekstowe (to co dostępne w szablonie
        }
    )