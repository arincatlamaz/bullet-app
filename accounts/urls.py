from django.conf.urls import url
from . import views

app_name = "accounts"

urlpatterns = [
        url(r'^registration$', views.registration_view, name='registration'),
        url(r'^login$', views.login_view, name='login'),
        url(r'^logout$', views.logout_view, name='logout'),
        url(r'^my_account', views.my_account_view, name='my_account'),
	url(r'^test$', views.test_view, name='test'),
]
