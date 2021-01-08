from django.shortcuts import redirect, render


def index(request):
    

    return render(
        request,
        "MainApp/index.html",  
        {
            'title' : "Main Page",            
        }
    )

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

def formularz(request):

    return render(
        request,
        "MainApp/formularz.html",
        {
            'title' : "Formularz dodawania ofert",
        }
    )



