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

class TextInput(forms.TextInput):

    input_type = 'text'

class NumberInput(forms.NumberInput):

    input_type = 'number'



class OfertyForm(forms.ModelForm):


    data = forms.DateField(widget=DateInput)
    czas_odjazdu = forms.TimeField(widget=TimeInput)
    cena = forms.IntegerField()
    ulica1 = forms.CharField(max_length=10, label='ulica poczatkowa')
    ulica2 = forms.CharField(max_length=10, label='ulica koncowa')
    numer_domu1 = forms.IntegerField(widget=NumberInput)
    numer_domu2 = forms.IntegerField(widget=NumberInput)
    kod_pocztowy1 = forms.CharField(max_length=6, label='kod poczatkowy')
    kod_pocztowy2 = forms.CharField(max_length=6, label='kod koncowy')

 
    def clean_cena(self):
        cena_passed = self.cleaned_data.get("cena")
        if cena_passed <= 0:
            raise forms.ValidationError("Podaj cene wiecej niz 0")
        return cena_passed


    class Meta:
        
        model = Oferty
        
        fields = ['data','czas_odjazdu','cena','ilosc_miejsc',
        'komentarz','ulica1','ulica2','numer_domu1','numer_domu2','kod_pocztowy1','kod_pocztowy2']



class OfertyFormKierowca(forms.ModelForm):


    data = forms.DateField(widget=DateInput)
    czas_odjazdu = forms.TimeField(widget=TimeInput)
    cena = forms.IntegerField()
    ulica1 = forms.CharField(max_length=10, label='ulica poczatkowa')
    ulica2 = forms.CharField(max_length=10, label='ulica koncowa')
    numer_domu1 = forms.IntegerField(widget=NumberInput)
    numer_domu2 = forms.IntegerField(widget=NumberInput)
    kod_pocztowy1 = forms.CharField(max_length=6, label='kod poczatkowy')
    kod_pocztowy2 = forms.CharField(max_length=6, label='kod koncowy')

 
    def clean_cena(self):
        cena_passed = self.cleaned_data.get("cena")
        if cena_passed <= 0:
            raise forms.ValidationError("Podaj cene wiecej niz 0")
        return cena_passed


    class Meta:
        
        model = Oferty
        
        fields = ['data','czas_odjazdu','cena','ilosc_miejsc',
        'komentarz','ulica1','ulica2','numer_domu1','numer_domu2','kod_pocztowy1','kod_pocztowy2']
