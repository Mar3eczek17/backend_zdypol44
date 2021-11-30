from django.shortcuts import render


class Dog:
    def __init__(self, name):
        self.name = name

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
            'fruits': fruits,
            'fruit': 'banan',
            'text': "<p style='color:red;'>Hello</p>",
            'passenger': {
                'name': "Bob",
                'age': 30,
            },
            'dog': Dog('Azor'),
        }
    )