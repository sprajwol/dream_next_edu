from django.views.generic import TemplateView

from about.models import Testimonial, Member
from test_prep.models import Course
from services.models import Service
from events.models import Event
# Create your views here.


class AboutView(TemplateView):
    template_name = 'about/about.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        if (Member.objects.all().exists()):
            members = Member.objects.all()
            context['members_data'] = members

        if (Course.objects.all().exists()):
            course_data = Course.objects.all()
            context['course_data'] = course_data

        if (Service.objects.all().exists()):
            services_data = Service.objects.all()
            context['services_data'] = services_data

        if (Event.objects.all().exists()):
            recent_events_data = Event.objects.all()[:3]
            context['show_event_popup'] = recent_events_data[0]

        context['about_page'] = 'active'
        return context
