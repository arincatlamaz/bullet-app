from django.contrib.auth import get_user_model
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), related_name='profile', on_delete=models.CASCADE, verbose_name='user')
    phone_number = models.CharField(max_length=20, verbose_name='Numer telefonu')

    class Meta:
        verbose_name = 'Profile'

    def __str__(self):
        return f'{self.user}s profile'
