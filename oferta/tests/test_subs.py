from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from oferta.models import Ad,Subscription
from os import path


class TestLive(TestCase):
    fixtures = [
        path.join('oferta', 'tests', 'fixtures','auth.json'),
        path.join('oferta', 'tests', 'fixtures', 'ad.json'),
    ]

    def test_subscrption_to_ad(self):
      
        #Sprawdzenie zarezerwowania pasazera
        user2 = get_user_model().objects.get(username='user2')
        self.client.force_login(user2)
        ad = Ad.objects.get(pk=1)
        url = reverse('subscribe_to_ad', kwargs={'pk': ad.pk})
        response = self.client.get(url)
        self.assertRedirects(response, reverse('ads-list'), fetch_redirect_response=False)

        sub = Subscription.objects.all().first()

        self.assertEqual(sub.ad, ad)
        self.assertEqual(sub.author, user2)
        self.assertEqual(sub.status, Subscription.INITIAL)

    def test_confirm_subscription(self):
        #Sprawdzenie potwierdzenia zarezerwowania kierowcem
        user1 = get_user_model().objects.get(username='user1')
        user2 = get_user_model().objects.get(username='user2')
        self.client.force_login(user1)
        ad = Ad.objects.get(pk=1)
        sub = Subscription(ad=ad, status=Subscription.INITIAL, author=user2)
        sub.save()
        url = reverse('confirm_subscribe', kwargs={'pk': sub.pk})
        response = self.client.get(url)
        self.assertRedirects(response, reverse('my-ads-list'))
        sub = Subscription.objects.get(pk=sub.pk)
        self.assertEqual(sub.status, Subscription.CONFIRMED)

    def test_reject_subscription(self):
        #Sprawdzenie odzucenia zarezerwowania kierowcem
        user1 = get_user_model().objects.get(username='user1')
        user2 = get_user_model().objects.get(username='user2')
        self.client.force_login(user1)
        ad = Ad.objects.get(pk=1)
        sub = Subscription(ad=ad, status=Subscription.INITIAL, author=user2)
        sub.save()
        url = reverse('reject_subscribe', kwargs={'pk': sub.pk})
        response = self.client.get(url)
        sub = Subscription.objects.get(pk=sub.pk)
        self.assertRedirects(response, reverse('my-ads-list'))
        self.assertEqual(sub.status, Subscription.REJECTED)

    def test_cancel_subscription(self):
        #Sprawdzenie anulowania zarezerwowania pasazerem
        user1 = get_user_model().objects.get(username='user1')
        user2 = get_user_model().objects.get(username='user2')
        self.client.force_login(user2)
        ad = Ad.objects.get(pk=1)
        sub = Subscription(ad=ad, status=Subscription.INITIAL, author=user2)
        sub.save()
        url = reverse('cancel_subscribe', kwargs={'pk': sub.pk})
        response = self.client.get(url)
        self.assertRedirects(response, reverse('my-ads-list'))
        self.assertEqual(Subscription.objects.filter(pk=sub.pk).count(), 0)

