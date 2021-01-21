from django.contrib.auth.models import User
from django import forms
from .models import Oferty

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']



class DateInput(forms.DateInput):

    input_type  = 'date'

class TimeInput(forms.TimeInput):
    
    input_type  = 'time'

class OfertyForm(forms.ModelForm):


    
    data = forms.DateField(widget=DateInput)
    czas_odjazdu = forms.TimeField(widget=TimeInput)
    czas_dojazdu = forms.TimeField(widget=TimeInput)
    
    
    class Meta:
        
        model = Oferty
        
        fields = ['data','czas_odjazdu','czas_dojazdu','cena','ilosc_miejsc',
        'komentarz','rodzaj_ofert']


    # def save(self):
    #     data = self.cleaned_data


