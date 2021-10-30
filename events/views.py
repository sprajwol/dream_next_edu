from django.views.generic import TemplateView, ListView, DetailView

from events.models import Event, Category
from test_prep.models import Course
# Create your views here.


class EventView(ListView):
    model = Event
    template_name = 'events/events.html'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        if (Course.objects.all().exists()):
            course_data = Course.objects.all()
            context['course_data'] = course_data

        context['events_page'] = 'active'
        return context


class EventDetailView(DetailView):
    model = Event
    template_name = 'events/events_single.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        if (Course.objects.all().exists()):
            course_data = Course.objects.all()
            context['course_data'] = course_data

        context['events_page'] = 'active'
        return context
