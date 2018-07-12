from django.views.generic import TemplateView

class LogoutView(TemplateView):
    template_name = 'bye.html'