from django.views.generic import TemplateView, ListView, DetailView

from services.models import Visa
# Create your views here.


class ServicesVisaListView(ListView):
    model = Visa
    template_name = 'services/services_visa.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        context['services_page'] = 'active'
        return context


class ServicesVisaDetailView(DetailView):
    model = Visa
    template_name = 'services/services_visa_specific.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        context['services_page'] = 'active'
        return context
