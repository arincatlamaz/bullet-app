from django.shortcuts import redirect, render, HttpResponse, get_object_or_404
from .models import Oferty, Uzytkownik
from .forms import OfertyForm, UserRegistrationForm
from django.contrib.auth import authenticate



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

def dodawanie_oferty(request):

    users = Uzytkownik.objects.all()
    print(users)

    if request.method == "POST":

        form = OfertyForm(request.POST)
        if form.is_valid():
            
            cd = form.cleaned_data

            oferty = Oferty()

            oferty.czas_dojazdu = cd.get('czas_dojazdu')

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

#def registration(request):
    
    #return render(request, 'MainApp/registration.html')
def register(request):
    if request.method == 'POST':
        print ('zarejestrował')
        user_form = UserRegistrationForm(request.POST)
        print (user_form.is_valid())
        print (user_form.cleaned_data)
        if user_form.is_valid():
            print('user form is valid')
            print(user_form.cleaned_data ['password'])
            print(user_form.cleaned_data ['email'])
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'MainApp/about.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'MainApp/registration.html', {'form': user_form})
