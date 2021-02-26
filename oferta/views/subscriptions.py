from django.core.exceptions import ValidationError
from django.views.generic import RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from oferta.models import Subscription, Ad

__all__ = ('CreateSubscribeView', 'ConfirmSubscribe', 'RejectSubscribe', 'CancelSubscribe')


class CreateSubscribeView(LoginRequiredMixin, RedirectView):
    pattern_name = 'ads-list'

    def get(self, request, *args, pk=None, **kwargs):
        ad = get_object_or_404(Ad, pk=pk, completed=False)
        if ad.author == self.request.user:
            raise ValidationError('Вы не можете подписываться на собственные объявления')
        if ad.subscriptions.filter(author=self.request.user).exists():
            raise ValidationError('Вы уже подписывались на это объявление')
        if ad.subscriptions.filter(status=Subscription.CONFIRMED).exists():
            raise ValidationError('Увы, свободных мест уже нет')

        obj = Subscription(author=self.request.user, ad=ad)
        obj.save()

        return super().get(request, *args, **kwargs)


class ConfirmSubscribe(LoginRequiredMixin, RedirectView):
    pattern_name = 'my-ads-list'

    def get(self, request, *args, pk=None, **kwargs):
        sub = get_object_or_404(Subscription, pk=pk, ad__author=self.request.user, status=Subscription.INITIAL)
        sub.status = Subscription.CONFIRMED
        sub.save()
        return super().get(request, *args, **kwargs)


class RejectSubscribe(LoginRequiredMixin, RedirectView):
    pattern_name = 'my-ads-list'

    def get(self, request, *args, pk=None, **kwargs):
        sub = get_object_or_404(Subscription, pk=pk, ad__author=self.request.user, status=Subscription.INITIAL)
        sub.status = Subscription.REJECTED
        sub.save()
        return super().get(request, *args, **kwargs)


class CancelSubscribe(LoginRequiredMixin, RedirectView):
    pattern_name = 'my-ads-list'

    def get(self, request, *args, pk=None, **kwargs):
        sub = get_object_or_404(Subscription, pk=pk, author=self.request.user, status=Subscription.INITIAL)
        sub.delete()
        return super().get(request, *args, **kwargs)
