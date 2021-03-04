from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

__all__ = ('Ad', 'Subscription')


class Ad(models.Model):
    DRIVER_KIND = 1
    PASSENGER_KIND = 2

    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='Author', related_name='ads')
    kind = models.SmallIntegerField(
        choices=(
            (DRIVER_KIND, 'Driver'), 
            (PASSENGER_KIND, 'Passenger'),
        ), verbose_name='kind'
    )
    created = models.DateTimeField(verbose_name='created at', auto_now_add=True)
    departure = models.DateTimeField(verbose_name='Data ta czas wyjazdu', null=False, blank=False)

    departure_postcode = models.CharField(max_length=5, verbose_name='Kod pocztowy (Punkt początkowy)',)
    departure_street = models.CharField(max_length=500, verbose_name='Ulica (Punkt początkowy)',)
    departure_home = models.CharField(max_length=50, verbose_name='Numer domu (Punkt początkowy)',)

    arrival_postcode = models.CharField(max_length=5, verbose_name='Kod pocztowy (Punkt docelowy)')
    arrival_street = models.CharField(max_length=500, verbose_name='Ulica (Punkt docelowy)')
    arrival_home = models.CharField(max_length=50, verbose_name='Numer domu (Punkt docelowy)')

    seats = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(20)],
        verbose_name='Ilość osób:' ,
    )

    price = models.DecimalField(max_digits=13, decimal_places=2, validators=[MinValueValidator(0)], verbose_name='Cena')

    car_model = models.CharField(max_length=50, verbose_name='Marka')

    comment = models.TextField(verbose_name='Komentarz', blank=True, default='')

    completed = models.BooleanField(verbose_name='Copmpleted', blank=True, default=False)

    @property
    def is_driver(self):
        return self.kind == self.DRIVER_KIND

    @property
    def is_passenger(self):
        return self.kind == self.PASSENGER_KIND

    class Meta:
        verbose_name = 'Ad'
        ordering = ('-created',)


class Subscription(models.Model):
    INITIAL = 1
    CONFIRMED = 2
    REJECTED = 3

    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='Author', related_name='subscriptions')
    ad = models.ForeignKey(Ad, on_delete=models.PROTECT, verbose_name='Ad', related_name='subscriptions')

    status = models.SmallIntegerField(
        choices=(
            (INITIAL, 'Initial'),
            (CONFIRMED, 'Confirmed'),
            (REJECTED, 'Rejected'),
        ), verbose_name='Status', blank=True, default=INITIAL
    )


