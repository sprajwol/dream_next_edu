from django.views.generic import TemplateView

from home.models import HeroSlider
from about.models import Testimonial
from events.models import Event
from test_prep.models import Course
# Create your views here.


class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        if (HeroSlider.objects.all().exists()):
            hero_sliders = HeroSlider.objects.all()
            context['hero_sliders'] = hero_sliders

        if (Testimonial.objects.all().exists()):
            testimonials = Testimonial.objects.all()
            context['testimonial_data'] = testimonials

        if (Event.objects.all().exists()):
            events = Event.objects.all()
            context['event_data'] = events

        if (Course.objects.all().exists()):
            course_data = Course.objects.all()
            context['course_data'] = course_data

        context['home_page'] = 'active'
        return context
