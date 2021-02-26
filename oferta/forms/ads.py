from django.forms import ModelForm, IntegerField, DateTimeInput
from oferta.models import Ad

__all__ = ('DriverAdForm', 'PassengerAdForm')

class AbstractDriverForm(ModelForm):
    kind = None

    def __init__(self, author=None, **kwargs):
        self.author = author
        super().__init__(**kwargs)

    def save(self, commit=True):
        if self.kind is None:
            raise NotImplementedError('Kind must be implemented!!!')

        self.instance.kind = self.kind
        self.instance.author = self.author
        return super().save(commit=commit)

    class Meta:
        model = Ad
        fields = [
            'departure',
            'departure_postcode', 'departure_street', 'departure_home',
            'arrival_postcode', 'arrival_street', 'arrival_home',
            'seats', 'price', 'car_model', 'comment',
        ]
        widgets = {
            'departure': DateTimeInput(attrs={
                'type': 'datetime-local'
            }, format='%Y-%m-%dT%H:%M'),
        }

class DriverAdForm(AbstractDriverForm):
    kind = Ad.DRIVER_KIND
    seats = IntegerField(max_value=20, min_value=1, label='Seats', help_text='Pick up the number of free seats')


class PassengerAdForm(AbstractDriverForm):
    kind = Ad.PASSENGER_KIND
    seats = IntegerField(max_value=20, min_value=1, label='Peoples', help_text='Count of peoples')
