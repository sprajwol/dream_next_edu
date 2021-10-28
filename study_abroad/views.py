from django.views.generic import TemplateView, ListView, DetailView

from study_abroad.models import Country
# Create your views here.


class StudyAbroadView(ListView):
    model = Country
    template_name = 'study_abroad/study_abroad.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        context['study_abroad_page'] = 'active'
        return context


class SingleCountryView(DetailView):
    model = Country
    template_name = 'study_abroad/single_country.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        context['study_abroad_page'] = 'active'
        return context
