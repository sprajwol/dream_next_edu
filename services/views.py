from django.views.generic import ListView, DetailView

from services.models import Service, Scholoarship
from test_prep.models import Course
from events.models import Event
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

        if (Scholoarship.objects.all().exists()):
            scholarships_data = Scholoarship.objects.all()
            context['scholarships_data'] = scholarships_data

        if (Event.objects.all().exists()):
            recent_events_data = Event.objects.all()[:3]
            context['show_event_popup'] = recent_events_data[0]

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

        if (Scholoarship.objects.all().exists()):
            scholarships_data = Scholoarship.objects.all()
            context['scholarships_data'] = scholarships_data

        if (Event.objects.all().exists()):
            recent_events_data = Event.objects.all()[:3]
            context['show_event_popup'] = recent_events_data[0]

        context['services_page'] = 'active'
        return context

class ScholarshipsDetailView(DetailView):
    model = Scholoarship
    template_name = 'services/scholarships_detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        
        if (Course.objects.all().exists()):
            course_data = Course.objects.all()
            context['course_data'] = course_data

        if (Service.objects.all().exists()):
            services_data = Service.objects.all()
            context['services_data'] = services_data

        if (Scholoarship.objects.all().exists()):
            scholarships_data = Scholoarship.objects.all()
            context['scholarships_data'] = scholarships_data

        if (Event.objects.all().exists()):
            recent_events_data = Event.objects.all()[:3]
            context['show_event_popup'] = recent_events_data[0]

        context['services_page'] = 'active'
        return context