from django.db import models
from django.dispatch import receiver
from djchoices import ChoiceItem, DjangoChoices
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UsernameField


# Create your models here.


class Role(models.Model):

    """Role"""

    role_id             = models.CharField(max_length=10, primary_key=True)
    pasazer             = models.BooleanField(default=False)
    kierowca            = models.BooleanField(default=False)


class Ocenianie(models.Model):

    """Ocenianie"""

    ocena_id            = models.CharField(max_length=10, primary_key=True)
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

    adres_id            = models.CharField(max_length=10, primary_key=True)
    wojewodztwo         = models.CharField(max_length=50)
    miejscowosc         = models.CharField(max_length=50)
    ulica               = models.CharField(max_length=50)
    numer_domu          = models.IntegerField()
    kod_pocztowy        = models.CharField(max_length=50, default=None)



class Trasa(models.Model):

    """Trasa"""
    
    trasa_id            = models.CharField(max_length=10, primary_key=True)
    adres_poczatkowy    = models.ForeignKey(Adres, related_name="adres_pocz", on_delete=models.CASCADE)
    adres_koncowy       = models.ForeignKey(Adres, related_name="adres_kon", on_delete=models.CASCADE)
    adres_spotkania     = models.ForeignKey(Adres, related_name="adres_spot", on_delete=models.CASCADE)



class Uzytkownik(models.Model):

    """Uzytkownik"""

    uzytkownik_imie     = models.CharField(max_length=50,null=True)
    uzytkownik_nazwisko = models.CharField(max_length=50,null=True)
    uzytkownik_telefon  = models.IntegerField(null=True)
    uzytkownik_mail     = models.EmailField(max_length=100,null=True)
    role_id             = models.ForeignKey(Role, name="role_id", on_delete=models.CASCADE,null=True)
    trasa_id            = models.ForeignKey(Trasa, name="trasa_id", on_delete=models.CASCADE,null=True)
    ocena_id            = models.ForeignKey(Ocenianie, name="ocena_id", on_delete=models.CASCADE,null=True)
    uzytkownik          = models.OneToOneField(User,default=None, on_delete = models.CASCADE,null=True)


    def __str__(self):
        return self.uzytkownik_imie


class Oferty(models.Model):

    """Oferty"""

    oferty_id           = models.CharField(max_length=10, primary_key=True)
    uzytkownik          = models.ForeignKey(Uzytkownik, on_delete=models.SET_NULL, null=True, blank=True, default = None)
    data                = models.DateField()
    czas_odjazdu        = models.TimeField()
    ilosc_miejsc        = models.IntegerField()
    cena                = models.IntegerField()
    komentarz           = models.CharField(max_length=100)
    trasa_id             = models.ForeignKey(Trasa, on_delete=models.CASCADE, default=None)
        


class Pojazd(models.Model):

    """Pojazd"""

    uzytkownik          = models.ForeignKey(Uzytkownik, on_delete=models.SET_NULL, null=True, blank=True, default = None)
    oferty_id           = models.ForeignKey(Oferty, name="oferty_id", on_delete=models.CASCADE)
    marka               = models.CharField(max_length=100)
    model               = models.IntegerField()


class History(models.Model):

    """History"""

    ocena_id            = models.ForeignKey(Ocenianie, name="ocena_id", on_delete=models.CASCADE)
    oferty_id           = models.ForeignKey(Oferty, name="oferty_id", on_delete=models.CASCADE)


class Trasaoferty(models.Model):

    """TrasaOferty"""

    trasa_id            = models.ForeignKey(Trasa, name="trasa_id", on_delete=models.CASCADE)
    oferty_id           = models.ForeignKey(Oferty, name="oferty_id", on_delete=models.CASCADE)

