from django.views.generic import TemplateView, ListView, DetailView

from study_abroad.models import Country
from test_prep.models import Course
from services.models import Service
# Create your views here.


class StudyAbroadView(ListView):
    model = Country
    template_name = 'study_abroad/study_abroad.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        if (Course.objects.all().exists()):
            course_data = Course.objects.all()
            context['course_data'] = course_data

        if (Service.objects.all().exists()):
            services_data = Service.objects.all()
            context['services_data'] = services_data

        context['study_abroad_page'] = 'active'
        return context


class SingleCountryView(DetailView):
    model = Country
    template_name = 'study_abroad/single_country.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        if (Course.objects.all().exists()):
            course_data = Course.objects.all()
            context['course_data'] = course_data
            
        if (Service.objects.all().exists()):
            services_data = Service.objects.all()
            context['services_data'] = services_data

        context['study_abroad_page'] = 'active'
        return context
