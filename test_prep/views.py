from django.views.generic import TemplateView

# Create your views here.


class TestPreparationView(TemplateView):
    template_name = 'test_prep/test_preparation.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        context['test_preparation_page'] = 'active'
        return context
