from django.test import SimpleTestCase
from django.urls import reverse, resolve
from MainApp.views import index,about,login,registration,dodawanie_oferty,ofertytras



class TestUrls(SimpleTestCase):

    def test_index_url_is_resolved(self):

        url = reverse('index')
        self.assertEquals(resolve(url).func, index)
    
    def test_about_url_is_resolved(self):

        url = reverse('about')
        self.assertEquals(resolve(url).func, about)
    
    def test_login_url_is_resolved(self):

        url = reverse('login')
        self.assertEquals(resolve(url).func, login)
    
    def test_registration_url_is_resolved(self):

        url = reverse('registration')
        self.assertEquals(resolve(url).func, registration)

    def test_dodawanie_oferty_url_is_resolved(self):

        url = reverse('dodawanie_oferty')
        self.assertEquals(resolve(url).func, dodawanie_oferty)
    
    def test_ofertytras_url_is_resolved(self):

        url = reverse('ofertytras')
        self.assertEquals(resolve(url).func, ofertytras)


