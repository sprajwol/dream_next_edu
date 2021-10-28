from django.views.generic import TemplateView, ListView, DetailView

from test_prep.models import Course
# Create your views here.


class TestPreparationView(ListView):
    model = Course
    template_name = 'test_prep/test_preparation.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        context['test_preparation_page'] = 'active'
        return context


class TestPreparationDetailView(DetailView):
    model = Course
    template_name = 'test_prep/single_test.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        context['study_abroad_page'] = 'active'
        return context
