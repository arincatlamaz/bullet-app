from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from MainApp import views, forms


app_name = "bullet"

urlpatterns = [


    url(r'^$', views.index, name='index'),
    url(r'^ofertytras$', views.ofertytras, name='ofertytras'),
    url(r'^home$', views.index, name='home'),
    url(r'^about$', views.about, name='about'),
    url(r'login$', views.login, name='login'),
    url(r'registration$', views.register, name='registration'),
    url(r'^form$', views.dodawanie_oferty, name='form'),
    url(r'^account', views.account, name='account'),
    url(r'^dodaj', views.dodaj, name='dodaj'),
    url(r'^Kierowca', views.Kierowca, name='Kierowca'),
    url(r'^Pasazer', views.Pasazer, name='Pasazer'),
    url(r'^oferta', views.oferta, name='oferta'),
    url(r'^obecne', views.obecne, name='obecne'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)




