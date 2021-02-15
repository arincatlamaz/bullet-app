from django.shortcuts import redirect, render, HttpResponse, get_object_or_404
from .models import Oferty, Uzytkownik, Adres, Trasa
from .forms import OfertyForm, UserRegistrationForm, OfertyFormKierowca
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

    oferty = Oferty.objects.get(uzytkownik_id=user.id)
    print(oferty)

    trasy_oferty = Trasa.objects.get(id=oferty.trasa_id)
    print(trasy_oferty)

    adres_pocz  = Adres.objects.get(id_pocz=trasy_oferty.adres_pocz)
    print(adres_pocz)



    


    return render(request, "MainApp/ofertytras.html", {'data':oferty2,})


##################----KIEROWCA-----####################

def dodawanie_oferty(request):
    
    if request.method == "POST":
        
        form = OfertyForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            
            cd = form.cleaned_data

            oferty = Oferty()

            
            adres_poczatkowy = Adres()
            adres_poczatkowy.ulica = cd.get('ulica1')
            adres_poczatkowy.numer_domu = cd.get('numer_domu1')
            adres_poczatkowy.kod_pocztowy = cd.get('kod_pocztowy1')

            adres_koncowy = Adres()
            adres_koncowy.ulica = cd.get('ulica2')
            adres_koncowy.numer_domu = cd.get('numer_domu2')
            adres_koncowy.kod_pocztowy = cd.get('kod_pocztowy2')

            trasa = Trasa()
            trasa.adres_poczatkowy = adres_poczatkowy
            trasa.adres_koncowy = adres_koncowy
            trasa.adres_spotkania = adres_poczatkowy



            oferty.czas_odjazdu = cd.get('czas_odjazdu')

            oferty.data = cd.get('data')

            oferty.ilosc_miejsc = cd.get('ilosc_miejsc')

            oferty.komentarz = cd.get('komentarz')

            oferty.cena = cd.get('cena')
            
            oferty.trasa = trasa
            print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
            print(adres_koncowy)
            print(adres_poczatkowy)
            print(trasa)
            print(oferty)
            print('-----------------------------------------------------------------')
            adres_poczatkowy.save()
            adres_koncowy.save()
            trasa.save()
            
            oferty.save()

            return redirect('about')
        else:
            print(form.errors)

    else:
        form = OfertyForm()
        

    return render(request, 'MainApp/Kierowca.html', {'form':form,})


####################----PASAZER-----#######################

def dodawanie_oferty_pasazer(request):
    
    if request.method == "POST":
        
        form = OfertyFormKierowca(request.POST)
        print(form.is_valid())
        if form.is_valid():
            
            cd = form.cleaned_data

            oferty = Oferty()

            
            adres_poczatkowy = Adres()
            adres_poczatkowy.ulica = cd.get('ulica1')
            adres_poczatkowy.numer_domu = cd.get('numer_domu1')
            adres_poczatkowy.kod_pocztowy = cd.get('kod_pocztowy1')

            adres_koncowy = Adres()
            adres_koncowy.ulica = cd.get('ulica2')
            adres_koncowy.numer_domu = cd.get('numer_domu2')
            adres_koncowy.kod_pocztowy = cd.get('kod_pocztowy2')

            trasa = Trasa()
            trasa.adres_poczatkowy = adres_poczatkowy
            trasa.adres_koncowy = adres_koncowy
            trasa.adres_spotkania = adres_poczatkowy



            oferty.czas_odjazdu = cd.get('czas_odjazdu')

            oferty.data = cd.get('data')

            oferty.ilosc_miejsc = cd.get('ilosc_miejsc')

            oferty.komentarz = cd.get('komentarz')

            oferty.cena = cd.get('cena')
            
            oferty.trasa = trasa
            print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
            print(adres_koncowy)
            print(adres_poczatkowy)
            print(trasa)
            print(oferty)
            print('-----------------------------------------------------------------')
            adres_poczatkowy.save()
            adres_koncowy.save()
            trasa.save()
            
            oferty.save()

            return redirect('about')
        else:
            print(form.errors)

    else:
        form = OfertyForm()
        

    return render(request, 'MainApp/Pasazer.html', {'form':form,})









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







def login(request):
    return render(request, 'MainApp/login.html')
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