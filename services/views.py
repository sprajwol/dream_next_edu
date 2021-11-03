from django.views.generic import TemplateView, ListView, DetailView

from services.models import Service
from test_prep.models import Course
# Create your views here.


class ServicesListView(ListView):
    model = Service
    template_name = 'services/services.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        if (Course.objects.all().exists()):
            course_data = Course.objects.all()
            context['course_data'] = course_data

        if (Service.objects.all().exists()):
            services_data = Service.objects.all()
            context['services_data'] = services_data

        context['services_page'] = 'active'
        return context

        
class ServicesDetailView(DetailView):
    model = Service
    template_name = 'services/services_detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        if (Course.objects.all().exists()):
            course_data = Course.objects.all()
            context['course_data'] = course_data

        if (Service.objects.all().exists()):
            services_data = Service.objects.all()
            context['services_data'] = services_data

        context['services_page'] = 'active'
        return context
