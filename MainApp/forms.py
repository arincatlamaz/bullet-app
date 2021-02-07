from django.contrib.auth.models import User
from django import forms
from .models import Oferty, Uzytkownik
from django.forms.widgets import PasswordInput
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields


class UserRegistrationForm(UserCreationForm):


    uzytkownik_imie = forms.CharField(max_length=50)
    uzytkownik_mail = forms.EmailField(required=True)

    class Meta(UserCreationForm):
        model = User
        fields = ["username", "email", "password1", "password2"]



class DateInput(forms.DateInput):

    input_type  = 'date'

class TimeInput(forms.TimeInput):
    
    input_type  = 'time'



class OfertyForm(forms.ModelForm):


    data = forms.DateField(widget=DateInput)
    czas_odjazdu = forms.TimeField(widget=TimeInput)
    czas_dojazdu = forms.TimeField(widget=TimeInput)
    cena = forms.IntegerField()

    def clean_cena(self):
        cena_passed = self.cleaned_data.get("cena")
        if cena_passed <= 0:
            raise forms.ValidationError("Podaj cene wiecej niz 0")
        return cena_passed


    class Meta:
        
        model = Oferty
        
        fields = ['data','czas_odjazdu','czas_dojazdu','cena','ilosc_miejsc',
        'komentarz','rodzaj_ofert']

# class Ofertytras(forms.ModelForm):


    


