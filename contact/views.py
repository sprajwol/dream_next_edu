from django.shortcuts import render
from django.views.generic import TemplateView

from test_prep.models import Course
from contact.models import Contact
from services.models import Service, Scholoarship
from events.models import Event
from study_abroad.models import Country
# Create your views here.


class ContactView(TemplateView):
    template_name = 'contact/contact.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        if (Course.objects.all().exists()):
            course_data = Course.objects.all()
            context['course_data'] = course_data
            
        if (Service.objects.all().exists()):
            services_data = Service.objects.all()
            context['services_data'] = services_data

        if (Event.objects.all().exists()):
            recent_events_data = Event.objects.all()[:3]
            context['show_event_popup'] = recent_events_data[0]

        if (Scholoarship.objects.all().exists()):
            scholarships_data = Scholoarship.objects.all()
            context['scholarships_data'] = scholarships_data

        context['contact_page'] = 'active'
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


class EnquiryView(TemplateView):
    template_name = 'contact/enquiry_form.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        if (Course.objects.all().exists()):
            course_data = Course.objects.all()
            context['course_data'] = course_data
            
        if (Service.objects.all().exists()):
            services_data = Service.objects.all()
            context['services_data'] = services_data

        if (Event.objects.all().exists()):
            recent_events_data = Event.objects.all()[:3]
            context['show_event_popup'] = recent_events_data[0]

        if (Scholoarship.objects.all().exists()):
            scholarships_data = Scholoarship.objects.all()
            context['scholarships_data'] = scholarships_data

        if (Country.objects.all().exists()):
            countries_data = Country.objects.all()
            context['countries_data'] = countries_data

        return context
