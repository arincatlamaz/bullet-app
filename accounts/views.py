from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from MainApp.models import Uzytkownik

# Create your views here.

def registration_view(request):

    if request.method == 'POST':
        registration_form = UserRegistrationForm(request.POST)
        if (registration_form.is_valid()):
            new_user = registration_form.save(commit=False)
            uzyt = Uzytkownik()
            uzyt.uzytkownik = new_user
            new_user.save()
            uzyt.save()
            login (request, new_user)
            redirect ('MainApp:about')
        else:
            print(registration_form.errors)
    else:
        registration_form = UserRegistrationForm()
    return render (request, 'accounts/registration.html', {'form' : registration_form})
