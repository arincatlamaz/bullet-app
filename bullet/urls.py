from django.conf.urls import include, url
from MainApp import views


urlpatterns = [


    url(r'^$', views.index, name='index'),
    url(r'^home$', views.index, name='home'),
    url(r'^about$', views.about, name='about'),
    url(r'^formularz$', views.formularz, name='formularz'),
]