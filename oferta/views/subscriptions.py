from django.core.exceptions import ValidationError
from django.urls import reverse
from django.views.generic import RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from oferta.models import Subscription, Ad

__all__ = ('CreateSubscribeView', 'ConfirmSubscribe', 'RejectSubscribe', 'CancelSubscribe')

from oferta.send_email import send_email


class CreateSubscribeView(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('ads-list')

    def get(self, request, *args, pk=None, **kwargs):
        ad = get_object_or_404(Ad, pk=pk, completed=False)
        if ad.author == self.request.user:
            raise ValidationError('Nie możesz zarezerwować swoją oferte')
        if ad.subscriptions.filter(author=self.request.user).exists():
            raise ValidationError('Jesteś już zarezerwowany na tą oferte')
        if ad.subscriptions.filter(status=Subscription.CONFIRMED).exists():
            raise ValidationError('Już nie ma wolnych miejsc')

        obj = Subscription(author=self.request.user, ad=ad)
        obj.save()

        send_email(
            self.request.user,
            "Dziękujemy za zarezerwowanie oferty!",
            "email/inf-zarezerw.html",
            {
                "title": "Dziękujemy za zarezerwowanie oferty!",
                "ad": ad,
            }
        )
        send_email(
            ad.author,
            "Zarezerwowana oferta",
            "email/zarezerwowal.html",
            {
                "title": "Zarezerwowana oferta",
                "user": self.request.user,
                "ad": ad,
            }
        )

        return super().get(request, *args, pk, **kwargs)


class ConfirmSubscribe(LoginRequiredMixin, RedirectView):
    pattern_name = 'my-ads-list'

    def get(self, request, *args, pk=None, **kwargs):
        sub = get_object_or_404(Subscription, pk=pk, ad__author=self.request.user, status=Subscription.INITIAL)
        sub.status = Subscription.CONFIRMED
        sub.save()

        send_email(
            sub.author,
            "Dziękujemy za zarezerwowanie oferty!",
            "email/zgoda.html",
            {
                "title": "Użytkownik podtwierdzil się podróż!",
                "email": self.request.user.email,
                "ad": sub.ad,
            }
        )

        return super().get(request, *args, **kwargs)


class RejectSubscribe(LoginRequiredMixin, RedirectView):
    pattern_name = 'my-ads-list'

    def get(self, request, *args, pk=None, **kwargs):
        sub = get_object_or_404(Subscription, pk=pk, ad__author=self.request.user, status=Subscription.INITIAL)
        sub.status = Subscription.REJECTED
        sub.save()

        send_email(
            sub.author,
            "Dziękujemy za zarezerwowanie oferty!",
            "email/odrzucenie.html",
            {
                "title": "Niestety użytkownik odmówił Ci w podróży!",
                "ad": sub.ad,
            }
        )

        return super().get(request, *args, **kwargs)


class CancelSubscribe(LoginRequiredMixin, RedirectView):
    pattern_name = 'my-ads-list'

    def get(self, request, *args, pk=None, **kwargs):
        sub = get_object_or_404(Subscription, pk=pk, author=self.request.user, status=Subscription.INITIAL)
        sub.delete()
        return super().get(request, *args, **kwargs)
