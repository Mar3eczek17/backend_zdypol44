from django.shortcuts import HttpResponse

def index(request):
    print(dir(request))

    return HttpResponse("Hello, world!")