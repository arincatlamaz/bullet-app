from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from oferta.models import Ad
from os import path

class TestLive(TestCase):
    fixtures = [path.join('oferta', 'tests', 'fixtures','auth.json'),]

    def test_create_ad_driver(self):
       
        #Sprawdzenie dodawania oferty jako kierowca
        
        self.client.force_login(get_user_model().objects.get(username='user1'))
        url = reverse('create_driver_ad')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        data = {
            'departure': '2021-03-01T12:30:00',
            'departure_postcode': '61709',
            'departure_street': 'aleja Niepodłeglośi ',
            'departure_home': "36",
            'arrival_postcode': "12453",
            'arrival_street': "ul Dfrabr",
            'arrival_home': "21",
            'seats': '2',
            'price': '3.99',
            'car_model': 'Toyota',
            'comment': 'No comments',
        }
        response = self.client.post(url, data=data)
        self.assertRedirects(response, reverse('ads-list'), fetch_redirect_response=False)
        self.assertEqual(Ad.objects.all().count(), 1)
        ad = Ad.objects.all().first()
        self.assertEqual(ad.kind, Ad.DRIVER_KIND)
        self.assertFalse(ad.completed)

    def test_create_ad_passenger(self):
       #Sprawdzenie dodawania oferty jako pasazer

        self.client.force_login(get_user_model().objects.get(username='user1'))
        url = reverse('create_passenger_ad')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        data = {
            'departure': '2021-03-01T12:30:00',
            'departure_postcode': '61709',
            'departure_street': 'aleja Niepodłeglośi ',
            'departure_home': "36",
            'arrival_postcode': "12453",
            'arrival_street': "ul Dfrabr",
            'arrival_home': "21",
            'seats': '2',
            'price': '3.99',
            'comment': 'No comments',
        }
        response = self.client.post(url, data=data)
        self.assertRedirects(response, reverse('ads-list'), fetch_redirect_response=False)

        self.assertEqual(Ad.objects.all().count(), 1)

        ad = Ad.objects.all().first()
       
        self.assertEqual(ad.kind, Ad.PASSENGER_KIND)
      
        self.assertFalse(ad.completed)
