from django.shortcuts import redirect, render, HttpResponse, get_object_or_404
from .models import Oferty, Uzytkownik
from .forms import OfertyForm, UserRegistrationForm
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django import forms




def index(request):

    return render(request, "MainApp/index.html",  
    {'title' : "Main Page",})

def about(request):

    return render(
        request,
        "MainApp/about.html",
        {
            'title' : "About MainApp",
            'message' : "This is a message",
            'content' : "Here will land more and more content."
        }
    )


def ofertytras(request):

    


    wszystkieoferty2 = Oferty.objects.all()[:2]

    context = {'wszystkieoferty2':wszystkieoferty2}

    


    return render(request, "MainApp/ofertytras.html", context)





def dodawanie_oferty(request):

    wszystkieoferty = Oferty.objects.all()
    print(wszystkieoferty)

    if request.method == "POST":
        

        form = OfertyForm(request.POST)
        if form.is_valid():
            
            
            
            cd = form.cleaned_data

            oferty = Oferty()

            oferty.czas_dojazdu = cd.get('czas_dojazdu')
            print(oferty.czas_dojazdu)

            oferty.czas_odjazdu = cd.get('czas_odjazdu')

            oferty.data = cd.get('data')

            oferty.ilosc_miejsc = cd.get('ilosc_miejsc')

            oferty.komentarz = cd.get('komentarz')

            oferty.cena = cd.get('cena')
            
            oferty.rodzaj_ofert = cd.get('rodzaj_ofert')
            
            


            
            oferty.save()
            print(oferty)

            return redirect('form')



    else:
        form = OfertyForm()


    return render(request, 'MainApp/form.html', {'form':form,})

def login(request):
    return render(request, 'MainApp/login.html')





def register(request):
    
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user = form.save(commit=False)
            print(user)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            print(username)
            print(password)
            profile = authenticate(username = username, password = password)
            print(profile)
            user.save()
            currentUser = Uzytkownik()
            currentUser.save() 
                      
            print(currentUser)
            
            return render(request, 'MainApp/about.html', {'new_user': new_user})
        else:
            print(user_form.errors)
    else:
        user_form = UserRegistrationForm()
    return render(request, 'MainApp/registration.html', {'form': user_form})

def account(request):
    return render(request, 'MainApp/account.html')

def dodaj(request):
    return render(request, 'MainApp/dodaj.html')

def Kierowca(request):
    return render(request, 'MainApp/Kierowca.html')

def Pasazer(request):
    return render(request, 'MainApp/Pasazer.html')

def oferta(request):
    return render(request, 'MainApp/oferta.html')

def obecne(request):
    return render(request, 'MainApp/obecne.html')   