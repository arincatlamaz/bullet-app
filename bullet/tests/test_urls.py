from django.test import TestCase

class LiveTest(TestCase):
    def test_index(self):
        response = self.client.get('/')
        self.assertTrue(response.status_code, 200)
