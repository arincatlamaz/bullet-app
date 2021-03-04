from django.core.exceptions import ValidationError
from django.db.models import OuterRef, Case, When, Value, Exists, SmallIntegerField, CharField
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView, RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin
from oferta.forms import DriverAdForm, PassengerAdForm, AdFilterForm
from oferta.models import Ad, Subscription

__all__ = (
    'AdKindSelectView', 'DriverAdCreateView', 'PassengerAdCreateView',
    'ActiveAdsList', 'AdUpdateView', 'AdDeleteView', 'MyAdsList', 'AdCompleteView',
    'MyHistoryAdsList'
)


class AdKindSelectView(LoginRequiredMixin, TemplateView):
    template_name = 'ads/AdKindSelect.html'


class AbstractAdCreateView(LoginRequiredMixin, CreateView):
    model = Ad
    success_url = reverse_lazy('ads-list')

    def get_form_kwargs(self):
        ctx = super().get_form_kwargs()
        ctx['author'] = self.request.user
        return ctx


class DriverAdCreateView(AbstractAdCreateView):
    form_class = DriverAdForm
    template_name = 'ads/driver_oferta.html'


class PassengerAdCreateView(AbstractAdCreateView):
    form_class = PassengerAdForm
    template_name = 'ads/passenger_oferta.html'


class ActiveAdsList(ListView):
    template_name = 'ads/actual_lists.html'

    def get_form(self):
        return AdFilterForm(self.request.GET)

    def get_queryset(self):
        ad_filter_form = self.get_form()
        if ad_filter_form.is_valid():
            kind = ad_filter_form.cleaned_data['kind'] or Ad.DRIVER_KIND
        else:
            kind = Ad.DRIVER_KIND
        return Ad.objects.filter(completed=False, kind=kind)

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super().get_context_data(object_list=object_list, **kwargs)
        ctx['form'] = self.get_form()
        return ctx

    context_object_name = 'ads'


class MyAdsList(LoginRequiredMixin, ListView):
    template_name = 'ads/my_lists.html'

    def get_queryset(self):
        subs_to_confirm = Subscription.objects.filter(ad=OuterRef('pk'), status=Subscription.INITIAL)
        subs_confirmed = Subscription.objects.filter(ad=OuterRef('pk'), status=Subscription.CONFIRMED)
        subs_non_rejected = Subscription.objects.filter(ad=OuterRef('pk'), status__in=(Subscription.CONFIRMED, Subscription.INITIAL))
        my_subs = Subscription.objects.filter(ad=OuterRef('pk'), author=self.request.user)
        my_q = Ad.objects.filter(author=self.request.user, completed=False)\
            .annotate(
                current_status=Case(
                    When(Exists(subs_to_confirm), then=Value(-1)),
                    When(Exists(subs_confirmed), then=Value(-2)),
                    default=Value(0),
                    output_field=SmallIntegerField()
                ),
                subscriber = subs_non_rejected.values('author__username')[:1],
                sub=subs_to_confirm.values('pk')[:1],
            )
        my_s = Ad.objects.filter(Exists(my_subs), completed=False).annotate(
            current_status = my_subs.values('status')[:1],
            subscriber = Value(None, output_field=CharField()),
            sub= my_subs.values('pk')[:1],
        )

        q = my_q.union(my_s, all=True)
        return q

    context_object_name = 'ads'

class MyHistoryAdsList(LoginRequiredMixin, ListView):
    template_name = 'ads/hist_lists.html'

    def get_queryset(self):
        subs_to_confirm = Subscription.objects.filter(ad=OuterRef('pk'), status=Subscription.INITIAL)
        subs_confirmed = Subscription.objects.filter(ad=OuterRef('pk'), status=Subscription.CONFIRMED)
        subs_non_rejected = Subscription.objects.filter(ad=OuterRef('pk'), status__in=(Subscription.CONFIRMED, Subscription.INITIAL))
        my_subs = Subscription.objects.filter(ad=OuterRef('pk'), author=self.request.user)
        my_q = Ad.objects.filter(author=self.request.user, completed=True)\
            .annotate(
                current_status=Case(
                    When(Exists(subs_to_confirm), then=Value(-1)),
                    When(Exists(subs_confirmed), then=Value(-2)),
                    default=Value(0),
                    output_field=SmallIntegerField()
                ),
                subscriber = subs_non_rejected.values('author__username')[:1],
                sub=subs_to_confirm.values('pk')[:1],
            )
        my_s = Ad.objects.filter(Exists(my_subs), completed=True).annotate(
            current_status = my_subs.values('status')[:1],
            subscriber = Value(None, output_field=CharField()),
            sub= my_subs.values('pk')[:1],
        )

        q = my_q.union(my_s, all=True)
        return q

    context_object_name = 'ads'


class AdCompleteView(LoginRequiredMixin, RedirectView):
    pattern_name = 'my-ads-list'

    def get(self, request, *args, pk=None, **kwargs):
        ad = get_object_or_404(Ad, pk=pk, completed=False)
        if ad.author != self.request.user and not ad.subscriptions.filter(author=self.request.user).exists():
            raise Http404

        ad.completed = True
        ad.save()
        return super().get(request, *args, **kwargs)



class AdUpdateView(LoginRequiredMixin, UpdateView):
    success_url = reverse_lazy('ads-list')

    def get_template_names(self):
        if self.object.kind == Ad.DRIVER_KIND:
            return 'ads/driver_oferta.html'
        if self.object.kind == Ad.PASSENGER_KIND:
            return 'ads/passenger_oferta.html'

        raise NotImplementedError('Unknown ad kind')

    def get_form_class(self):
        if self.object.kind == Ad.DRIVER_KIND:
            return DriverAdForm
        if self.object.kind == Ad.PASSENGER_KIND:
            return PassengerAdForm

        raise NotImplementedError('Unknown ad kind')

    def get_form_kwargs(self):
        ctx = super().get_form_kwargs()
        ctx['author'] = self.request.user
        return ctx

    # def get_context_data(self, **kwargs):
    #     ctx = super(AdUpdateView, self).get_context_data(**kwargs)
    #     ctx['is_update'] = True
    #     return ctx

    def get_queryset(self):
        return Ad.objects.filter(completed=False, author=self.request.user)


class AdDeleteView(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('ads-list')

    def get(self, request, *args, **kwargs):
        ad= get_object_or_404(Ad, pk=kwargs.get('pk'), author=self.request.user)
        ad.delete()
        return super().get(request, *args, **kwargs)
