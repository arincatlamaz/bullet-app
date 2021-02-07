from django.test import TestCase, Client
from django.urls import reverse
from MainApp.models import Role, Ocenianie, Adres, Trasa, Uzytkownik, Oferty
import json 


class TestViews(TestCase):

    def setUp(self):

        self.oferty = Oferty()

        
  
    def test_views_dodawanieoferty(self):

        ofert12 = Oferty.objects.all()[:1]
        
        self.assertIsNotNone(ofert12, None)


    



# request.method
# is_valid