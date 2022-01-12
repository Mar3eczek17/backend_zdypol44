from django.urls import path
from django.views.generic import TemplateView

from viewapp import views

app_name = 'viewapp'

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('hello2/', views.HelloView.as_view(), name='hello2'),

    path('template/hello/', views.template_hello, name='template-hello'),
    path('template/hello2/', views.HelloClassView.as_view, name='template-hello2'),
    path('template/hello3/', views.HelloGenericView.as_view, name='template-hello3'),

    path(
        'template/hello4/',
        views.TemplateView.as_view(template_name='viewapp/hello.html'),
        name='template-hello4'
    ),

    path('template2/hello/', views.template_hello2, name='template-hello2'),
    path('template2/hello2/', views.HelloClassView2.as_view, name='template2-hello'),
    path('template2/hello3/', views.HelloGenericView2.as_view(), name='template2-hello3'),

    path('person/<int:id>', views.person_detail, name='person-detail'),
    path('person2/<int:id>', views.PersonView.as_view, name='person-detail2'),
    # Dla widoku generycznego (detailView) zmienna w konwerterze funkcji path musi nazywać się pk
    path('person3/<int:pk>', views.PersonDetailView.as_view, name='person-detail3'),

    path('create-person/', views.create_person, name='create-person'),
    path('create-person2/', views.PersonCreateView.as_view(), name='create-person2'),
    path('create-person3/', views.PersonGenericCreateView.as_view(), name='create-person3'),
]