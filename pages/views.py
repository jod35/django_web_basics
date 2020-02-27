from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name='pages/index.html'

class AboutPage(TemplateView):
    template_name='pages/about.html'