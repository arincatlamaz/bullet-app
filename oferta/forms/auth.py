from django.forms import CharField
from django.contrib.auth.forms import (
    UserCreationForm as BaseUserCreationForm,
    UserChangeForm as BaseUserChangeForm
)

__all__ = ('UserCreationForm', 'ProfileForm')

from oferta.models import Profile


class UserCreationForm(BaseUserCreationForm):
    class Meta(BaseUserCreationForm.Meta):
        fields = (*BaseUserCreationForm.Meta.fields, 'email')



class ProfileForm(BaseUserChangeForm):
    phone = CharField(max_length=20, required=False)
    password = None

    def __init__(self, *args, initial=dict, instance=None, **kwargs):
        if instance is not None:
            try:
                profile = instance.profile
            except Profile.DoesNotExist:
                profile = Profile(user=instance)

        super().__init__(*args, initial={**initial, 'phone': profile.phone_number}, instance=instance, **kwargs)

    class Meta(BaseUserChangeForm.Meta):
        fields = ('username', 'email', 'phone')
