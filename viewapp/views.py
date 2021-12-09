from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views import View
from viewapp.models import Person
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView


# Widoki generyczne
from django.views.generic import TemplateView



# funkcjon based view (Widok funkcyjny)
def hello(request):
    return HttpResponse("Hello, world!")

# class-based view (widok klasowy)
class HelloView(View):
    def get(self, request):
        return HttpResponse("Hello, world!")

def template_hello(request):
    return render(
        request,
        'viewapp/hello.html',
    )

# Widok klasowy
class HelloClassView(View):
    def get(self, request):
        return render(
            request,
            'viewapp/hello.html'
        )

# Generic view - Widok generyczny
class HelloGenericView(TemplateView):
    template_name = 'viewapp/hello'

# Widok funkcyjny
def template_hello2(request):
    name = "Adam"
    return render(
        request,
        'viewapp/hello.html',
        context={
            "name": name
        }
    )

# Widok klasowy
class HelloClassView2(View):
    def get(self, request):
        name = "Adam"

        return render(
            request,
            'viewapp/hello2.html',
            context={
                "name": name
            }
        )

# Widok generyczny
class HelloGenericView2(TemplateView):
    template_name = "viewapp/hello2.html"
    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['name'] = "Adam"
        return contex


# Widok funkcyjny
def person_detail(request, id):
    person = get_object_or_404(Person, id=id)

    return render(
        request,
        'viewapp/person_detail.html',
        context={
            "person": person
        }
    )

# Widok klasowy
class PersonView(View):
    def get(self, request, id):
        person = get_object_or_404(Person, id=id)

        return render(
            request,
            'viewapp/person_detail.html',
            context={
                "person": person
            }
        )

# Widok generyczny
class PersonDetailView(DetailView):
    model = Person
