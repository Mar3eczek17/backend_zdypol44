from django.shortcuts import render, redirect

from formapp.forms import ContactForm
from formapp.models import Message
from formapp.forms import MessageForm



# Formularz HTML
def contact1(reqest):
    if reqest.method == "POST":  # krok po form1
        print(reqest.POST)  # krok po form1
        data = reqest.POST

        # if "@" not in data.get('email'):
        #     return HttpResponse("Niepoprawny adres email")

        Message.objects.create(
            name=data.get('name'),
            email=data.get('email'),
            category=data.get('category'),
            subject=data.get('body'),
            body=data.get('body'),
            date=data.get('date'),
            time=data.get('time'),
        )

        return redirect('formapp:contact1')  # na koniec przekierowanie po krok po form1


    return render(
        reqest,
        'formapp/form1.html',
    )

#  krok 4
def contact2(request):

    if request.method == "POST":
        form = ContactForm(request.POST)  # bound - formularz związany
        if form.is_valid():
            data = form.cleaned_data

            Message.objects.create(
                name=data.get('name'),
                email=data.get('email'),
                category=data.get('category'),
                subject=data.get('subject'),
                body=data.get('body'),
                date=data.get('date'),
                time=data.get('time'),
            )
            return redirect("formapp:contact2")


    form = ContactForm() # wyswietlamy pusty formularz metoda get # unbound - formularz niezwiazany

    return render(
        request,
        'formapp/form2.html',
        context={
            'form': form,
        }
    )


# Formularze modelu Django
def contact3(request):

    if request.method == "POST":
        form = MessageForm(request.POST)
        form.save()

    form = MessageForm()

    return render(
        request,
        'formapp/form3.html',
        context={"form": form}
    )