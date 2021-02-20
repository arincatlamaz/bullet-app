from django.db import models
from django.dispatch import receiver
from djchoices import ChoiceItem, DjangoChoices
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.


class Role(models.Model):

    """Role"""

    role_id             = models.IntegerField(primary_key=True)
    pasazer             = models.BooleanField(default=False)
    kierowca            = models.BooleanField(default=False)


class Ocenianie(models.Model):

    """Ocenianie"""

    ocena_id            = models.IntegerField(primary_key=True)
    PUNKTOWANIE = (
        ('1', 'Bardzo Zle'),
        ('2', 'Zle'),
        ('3', 'Umiarkowany'),
        ('4', 'Dobrze'),
        ('5', 'Bardzo Dobrze'),
    )
    punkt = models.CharField(max_length=60, choices=PUNKTOWANIE)


class Adres(models.Model):

    """Adres"""

    adres_id            = models.IntegerField(primary_key=True)
    wojewodztwo         = models.CharField(max_length=50)
    miejscowosc         = models.CharField(max_length=50)
    ulica               = models.CharField(max_length=50)
    numer_domu          = models.IntegerField()


class Trasa(models.Model):

    """Trasa"""

    trasa_id            = models.IntegerField(primary_key=True)
    adres_poczatkowy    = models.ForeignKey(Adres, related_name="adres_pocz", on_delete=models.CASCADE)
    adres_koncowy       = models.ForeignKey(Adres, related_name="adres_kon", on_delete=models.CASCADE)
    adres_spotkania     = models.ForeignKey(Adres, related_name="adres_spot", on_delete=models.CASCADE)
    data                = models.DateTimeField(auto_now=True)



class Uzytkownik(models.Model):

    """Uzytkownik"""

    uzytkownik_imie     = models.CharField(max_length=50)
    uzytkownik_nazwisko = models.CharField(max_length=50)
    uzytkownik_telefon  = models.IntegerField(default=0)
    uzytkownik_mail     = models.EmailField(max_length=100)
    role            = models.ForeignKey(Role, null=True, on_delete=models.SET_NULL)
    trasa           = models.ForeignKey(Trasa, null=True, on_delete=models.SET_NULL)
    ocena           = models.ForeignKey(Ocenianie, null=True, on_delete=models.SET_NULL)
    uzytkownik = models.OneToOneField(User, on_delete = models.CASCADE)


    def __str__(self):
        return self.uzytkownik_imie


class Oferty(models.Model):

    """Oferty"""
    uzytkownik       = models.ForeignKey(Uzytkownik, on_delete=models.SET_NULL, null=True, blank=True, default = None)
    data                = models.DateField()
    czas_odjazdu        = models.TimeField()
    czas_dojazdu        = models.TimeField()
    ilosc_miejsc        = models.IntegerField()
    cena                = models.IntegerField()
    komentarz           = models.CharField(max_length=100)
    


    RODZAJE     = (
        ('1', 'Pasazer'),
        ('2', 'Kierowca'),
    )
    
    rodzaj_ofert        = models.CharField(max_length=50, choices=RODZAJE)

