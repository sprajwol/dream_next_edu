from django.views.generic import TemplateView

# Create your views here.


class ServicesVisaView(TemplateView):
    template_name = 'services/services_visa.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        context['services_page'] = 'active'
        return context
