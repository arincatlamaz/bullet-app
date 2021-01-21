from django.conf.urls import include, url
from MainApp import views, forms

app_name = "bullet"

urlpatterns = [


    url(r'^$', views.index, name='index'),
    url(r'^home$', views.index, name='home'),
    url(r'^about$', views.about, name='about'),
    url(r'^form$', views.dodawanie_oferty, name='form'),
    

]