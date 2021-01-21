from django.contrib.auth.forms import UsernameField
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from djchoices import ChoiceItem, DjangoChoices
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
    adres_id            = models.IntegerField()
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
    uzytkownik_telefon  = models.IntegerField()
    uzytkownik_mail     = models.EmailField(max_length=100)
    role_id             = models.ForeignKey(Role, name="role", on_delete=models.CASCADE)
    trasa_id            = models.ForeignKey(Trasa, name="trasa_id", on_delete=models.CASCADE)
    ocena_id            = models.ForeignKey(Ocenianie, name="ocena_id", on_delete=models.CASCADE)
    uzytkownik = models.OneToOneField(User,on_delete = models.CASCADE)

















