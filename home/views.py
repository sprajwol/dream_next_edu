from django.shortcuts import render
from django.views.generic import TemplateView

from home.models import HeroSlider
from about.models import Testimonial
from events.models import Event
from contact.models import Contact


from test_prep.models import Course
from services.models import Service
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
            context['show_event_popup'] = events[0]

        if (Course.objects.all().exists()):
            course_data = Course.objects.all()
            context['course_data'] = course_data
            
        if (Service.objects.all().exists()):
            services_data = Service.objects.all()
            context['services_data'] = services_data

        context['home_page'] = 'active'
        return context

    def post(self, request):
        full_name = request.POST["full_name"]
        number = request.POST["contact_number"]
        email = request.POST["email"]
        # print("aaa", request.POST)
        # print("aaa", request.POST["your-service"])
        about = request.POST["your-service"]
        message = request.POST["message"]
        # print("lavis")

        new_contact = Contact()
        new_contact.full_name = full_name
        new_contact.email = email
        new_contact.contact = number
        new_contact.about = about
        new_contact.message = message
        new_contact.save()

        return render(request, self.template_name)
