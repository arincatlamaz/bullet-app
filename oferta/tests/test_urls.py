from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from oferta.models import Ad


class TestLive(TestCase):
    def test_about(self):
        #Strona jest otwarta bez blędów
        url = reverse('about')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
