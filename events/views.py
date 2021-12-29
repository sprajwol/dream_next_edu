from django.views.generic import TemplateView, ListView, DetailView

from events.models import Event, Category
from test_prep.models import Course
from latestnews.models import News
from services.models import Service
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
            
        if (Service.objects.all().exists()):
            services_data = Service.objects.all()
            context['services_data'] = services_data

        if (Category.objects.all().exists()):
            event_category_data = Category.objects.all()
            context['event_category_data'] = event_category_data

        if (News.objects.all().exists()):
            news_data = News.objects.all()[:3]
            context['news_data'] = news_data

        if (Event.objects.all().exists()):
            recent_events_data = Event.objects.all()[:3]
            context['show_event_popup'] = recent_events_data[0]

        context['events_page'] = 'active'
        return context

    def get_queryset(self):
        queryset = super().get_queryset()

        if self.kwargs.get('slug'):
            cat = Category.objects.get(slug=self.kwargs.get('slug'))
            queryset = queryset.filter(category=cat)

        return queryset


class EventDetailView(DetailView):
    model = Event
    template_name = 'events/events_single.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        if (Course.objects.all().exists()):
            course_data = Course.objects.all()
            context['course_data'] = course_data

        if (Category.objects.all().exists()):
            event_category_data = Category.objects.all()
            context['event_category_data'] = event_category_data

        if (Event.objects.all().exists()):
            recent_events_data = Event.objects.all()[:3]
            context['show_event_popup'] = recent_events_data[0]

        context['events_page'] = 'active'
        return context
