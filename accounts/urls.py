from django.conf.urls import url
from . import views
app_name = "accounts"

urlpatterns = [
        url(r'^registration$', views.registration_view, name='registration'),
]
