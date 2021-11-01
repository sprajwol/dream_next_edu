from django.shortcuts import render
from django.views.generic import TemplateView

from test_prep.models import Course
from contact.models import Contact
# Create your views here.


class ContactView(TemplateView):
    template_name = 'contact/contact.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        if (Course.objects.all().exists()):
            course_data = Course.objects.all()
            context['course_data'] = course_data

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
