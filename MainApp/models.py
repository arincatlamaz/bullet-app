from django.db import models
from django.dispatch import receiver
from djchoices import ChoiceItem, DjangoChoices
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UsernameField


# Create your models here.


class Role(models.Model):

    """Role"""


    pasazer             = models.BooleanField(default=False, null=True)
    kierowca            = models.BooleanField(default=False, null=True)


class Ocenianie(models.Model):

    """Ocenianie"""

    PUNKTOWANIE = (
        ('1', 'Bardzo Zle'),
        ('2', 'Zle'),
        ('3', 'Umiarkowany'),
        ('4', 'Dobrze'),
        ('5', 'Bardzo Dobrze'),
    )
    punkt               = models.CharField(max_length=60, choices=PUNKTOWANIE, null=True)


class Adres(models.Model):

    """Adres"""


    wojewodztwo         = models.CharField(max_length=50, null=True)
    miejscowosc         = models.CharField(max_length=50, null=True)
    ulica               = models.CharField(max_length=50, null=True)
    numer_domu          = models.IntegerField(null=True)


class Trasa(models.Model):

    """Trasa"""

    adres_poczatkowy    = models.ForeignKey(Adres, related_name="adres_pocz", on_delete=models.CASCADE, null=True)
    adres_koncowy       = models.ForeignKey(Adres, related_name="adres_kon", on_delete=models.CASCADE, null=True)
    adres_spotkania     = models.ForeignKey(Adres, related_name="adres_spot", on_delete=models.CASCADE, null=True)
    data                = models.DateTimeField(auto_now=True, null=True)



class Uzytkownicy(models.Model):

    """Uzytkownik"""
    
    uzytkownik_imie     = models.CharField(max_length=50, null=True)
    uzytkownik_nazwisko = models.CharField(max_length=50, null=True)
    uzytkownik_telefon  = models.IntegerField(null=True)
    uzytkownik_mail     = models.EmailField(max_length=100, null=True)
    role                = models.ForeignKey(Role, on_delete=models.CASCADE, null=True)
    trasa               = models.ForeignKey(Trasa, on_delete=models.CASCADE, null=True)
    ocena               = models.ForeignKey(Ocenianie, on_delete=models.CASCADE, null=True)
    uzytkownik          = models.OneToOneField(User,default=None, on_delete = models.CASCADE, null=True)


    def __str__(self):
        return self.uzytkownik_imie


class Oferty(models.Model):

    """Oferty"""


    uzytkownik          = models.ForeignKey(Uzytkownicy, on_delete=models.SET_NULL, null=True, blank=True, default = None)
    data                = models.DateField(null=True)
    czas_odjazdu        = models.TimeField(null=True)
    czas_dojazdu        = models.TimeField(null=True)
    ilosc_miejsc        = models.IntegerField(null=True)
    cena                = models.IntegerField(null=True)
    komentarz           = models.CharField(max_length=100, null=True)
    


    RODZAJE     = (
        ('1', 'Pasazer'),
        ('2', 'Kierowca'),
    )
    
    rodzaj_ofert        = models.CharField(max_length=50, choices=RODZAJE, null=True)



class Pojazd(models.Model):

    """Pojazd"""

    uzytkownik          = models.ForeignKey(Uzytkownicy, on_delete=models.SET_NULL, null=True, blank=True, default = None)
    oferty              = models.ForeignKey(Oferty, name="oferty_id", on_delete=models.CASCADE, null=True)
    marka               = models.CharField(max_length=100, null=True)
    model               = models.IntegerField(null=True)