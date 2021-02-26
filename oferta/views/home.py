from django.views.generic import TemplateView

__all__ = ('AboutView',)


class AboutView(TemplateView):
    template_name = 'about.html'
