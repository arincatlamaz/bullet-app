from django import forms
from .models import Oferty

class DateInput(forms.DateInput):

    input_type  = 'date'

class TimeInput(forms.TimeInput):
    
    input_type  = 'time'

class OfertyForm(forms.ModelForm):


    
    data = forms.DateField(widget=DateInput)
    czas_odjazdu = forms.TimeField(widget=TimeInput)
    czas_dojazdu = forms.TimeField(widget=TimeInput)
    
    def verify(self):
        if self.cena <= 0:
            
            return False

    class Meta:
        
        model = Oferty
        
        fields = ['data','czas_odjazdu','czas_dojazdu','cena','ilosc_miejsc',
        'komentarz','rodzaj_ofert']


    # def save(self):
    #     data = self.cleaned_data

    

