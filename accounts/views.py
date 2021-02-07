from django.shortcuts import render, redirect, reverse
from .forms import UserRegistrationForm
from MainApp.models import Uzytkownik
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm

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
            return redirect ('about')
        else:
            print(registration_form.errors)
    else:
        registration_form = UserRegistrationForm()
    return render (request, 'accounts/registration.html', {'form' : registration_form, 'title' : 'Rejestracja'})
    
def login_view(request):
    if request.method == 'POST':
        auth_form = AuthenticationForm(data=request.POST)
        if auth_form.is_valid():
            user = form.get_user()
            login (request, user)
            return redirect('about')
        else:
            print(auth_form.errors)
    else:
        auth_form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form' : auth_form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect ('about')

def my_account_view(request):
    return render(request, 'accounts/test.html')

def test_view(request):
    return render (request, 'accounts/test.html')
