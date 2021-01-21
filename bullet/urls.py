from django.conf.urls import include, url
from MainApp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [


    url(r'^$', views.index, name='index'),
    url(r'^home$', views.index, name='home'),
    url(r'^about$', views.about, name='about'),
    url(r'^formularz$', views.formularz, name='formularz'),
    url(r'login$', views.login, name='login'),
    url(r'registration$', views.register, name='registration'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)