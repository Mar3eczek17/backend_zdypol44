# krok 2
from django import forms
from django.forms.widgets import NumberInput
from formapp.models import Message

# Formularz Django
class ContactForm(forms.Form):
    CHOICES = [
        ("question", "Pytanie"),
        ("other", "Inne")
    ]

    name = forms.CharField(label="Imię")
    email = forms.EmailField(label="Email")
    category = forms.ChoiceField(choices=CHOICES, label="Kategoria")
    subject = forms.CharField(label="Temat")
    # body = forms.CharField(label="Treść", widget=forms.Textarea)
    body = forms.CharField(
        label="Treść", widget=forms.Textarea(attrs={'cols': 40, 'rows': 10}))
    date = forms.DateField(label="Ulubiona data", widget=NumberInput(attrs={"type": "date"}))
    time = forms.TimeField(label="Ulubiona godzina", widget=NumberInput(attrs={"type": "time"}))


# Formularz modelu
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        # fields = ['name', 'email', ...]
        # exclude = ['body']
        fields = "__all__"
        labels = {
            "name": "Imię",
            "email": "Email",
            "category": "Kategoria",
            "subject": "Tytuł",
            "body": "Treść",
            "date": "Ulubiona data",
            "time": "Ulubiona godzina",
        }
        widgets = {
            "date": NumberInput(attrs={'type':'date'}),
            "time": NumberInput(attrs={'type':'time'})
        }


