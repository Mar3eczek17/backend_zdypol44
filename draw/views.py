from django.shortcuts import render
import random

# Create your views here.
def toto_lotek_view(request):

    liczby = []
    i = 0
    while i < 6:
        liczba = random.randint(1, 49)
        if liczby.count(liczba) == 0:
            liczby.append(liczba)
            i += 1
    liczby_koncowe = ', '.join([str(x) for x in liczby])


    return render(
        request,
        'draw/toto-lotek.html',

        context={
            'liczby': str(liczby_koncowe),
        }
    )
