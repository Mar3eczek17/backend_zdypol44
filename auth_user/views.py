import logging

from django.shortcuts import render, HttpResponse


from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def cookies(request):
    print(request.COOKIES)
    res = HttpResponse("OK")
    res.set_cookie('title', 'Bosh')
    res.set_cookie('ciasteczko2', 10, max_age=1000)

    return res

def session(request):
    # print(dir(request))
    # print(dir(request.session))
    # print(request.session.session_key)
    session_id = request.session._get_or_create_session_key()
    res = HttpResponse("OK")
    res.set_cookie("sessionid", session_id)

    num_visit = request.session.get('num_visit', 0) + 1
    request.session['num_visit'] = num_visit
    return HttpResponse(f"Liczba odwiedzin: {num_visit}")

def index(request):
    users = User.objects.all()
    print(users)

    # Tworzenie użytkownika
    # adam = User.objects.create_user('adam', password='tajne')

    users = User.objects.all()
    print(users)

    # Uwierzytelnienie użytkownika
    authenticated_user = authenticate(username='adam', password='tajne')
    # print(type(result))

    # logowanie użytkownika
    if authenticated_user:
        login(request, user=authenticated_user)

    # Wylogowanie sie uzytkownika
    logout(request)

    return render(
        request,
        'auth_user/home.html'
    )




