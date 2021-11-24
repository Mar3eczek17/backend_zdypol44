from datetime import date
from django.shortcuts import render


# Create your views here.
def index(request):

    is_it_monday = False

    if date.today().weekday() == 2:  # 0 = Monday, 1 = Tues, etc.
        # Which both have a weekday and isoweekday methods.
        # weekday count from Monday = 0,
        # while isoweekday count from Monday = 1:
        is_it_monday = True

    return render(
        request,
        'isitmonday/index.html',
        context={
            'is_it_monday': is_it_monday,
        }
    )
