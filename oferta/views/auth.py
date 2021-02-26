from django.contrib.auth import get_user_model, login
from django.urls import reverse_lazy, reverse
from django.views.generic import FormView, TemplateView, UpdateView, RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout

from oferta.forms import UserCreationForm, ProfileForm
from oferta.models import Profile

__all__ = ('RegistrationView', 'ProfileView', 'UserChangeView', 'LogoutView')

class RegistrationView(FormView):
    form_class = UserCreationForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        form.save()
        login(self.request, form.instance)
        return super().form_valid(form)


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        try:
            profile = self.request.user.profile
        except Profile.DoesNotExist:
            profile = Profile(user=self.request.user)
            # profile.save()
            # ctx['user'] = self.request.user
        ctx['profile'] = profile
        return ctx


class UserChangeView(LoginRequiredMixin, UpdateView):
    template_name = 'accounts/zmien.html'
    form_class = ProfileForm
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return get_user_model().objects.get(pk = self.request.user.id)

    def form_valid(self, form):
        user = self.request.user
        try:
            profile = user.profile
        except Profile.DoesNotExist:
            profile = Profile(user=self.request.user)
        user.username = form.cleaned_data['username']
        user.email = form.cleaned_data['email']
        profile.phone_number = form.cleaned_data['phone']
        user.save()
        profile.save()
        return super().form_valid(form)


class LogoutView(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        logout(self.request)
        return reverse('index')
