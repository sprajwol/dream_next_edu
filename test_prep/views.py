from django.views.generic import TemplateView, ListView, DetailView

from test_prep.models import Course
from latestnews.models import News
from events.models import Event
from services.models import Service
# Create your views here.


class TestPreparationView(ListView):
    model = Course
    template_name = 'test_prep/test_preparation.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        if (Course.objects.all().exists()):
            course_data = Course.objects.all()
            context['course_data'] = course_data

        if (Service.objects.all().exists()):
            services_data = Service.objects.all()
            context['services_data'] = services_data

        if (News.objects.all().exists()):
            news_data = News.objects.all()[:3]
            context['news_data'] = news_data

        if (Event.objects.all().exists()):
            recent_events_data = Event.objects.all()[:3]
            context['recent_events_data'] = recent_events_data

        context['test_preparation_page'] = 'active'
        return context


class TestPreparationDetailView(DetailView):
    model = Course
    template_name = 'test_prep/single_test.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        if (Course.objects.all().exists()):
            course_data = Course.objects.all()
            context['course_data'] = course_data

        context['study_abroad_page'] = 'active'
        return context
