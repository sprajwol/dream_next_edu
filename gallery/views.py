from django.views.generic import TemplateView, DetailView, ListView

from gallery.models import Album
from services.models import Service
from test_prep.models import Course
# Create your views here.


class GalleryView(ListView):
    model = Album
    template_name = 'gallery/gallery.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        
            
        if (Course.objects.all().exists()):
            course_data = Course.objects.all()
            context['course_data'] = course_data
            
        if (Service.objects.all().exists()):
            services_data = Service.objects.all()
            context['services_data'] = services_data

        context['gallery_page'] = 'active'

        return context


class AlbumView(DetailView):
    model = Album
    template_name = 'gallery/album.html'

    def get_object(self, queryset=None):
        return Album.objects.get(photo_album_name_slug=self.kwargs.get("photo_album_name_slug"))

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        if (Course.objects.all().exists()):
            course_data = Course.objects.all()
            context['course_data'] = course_data

        if (Service.objects.all().exists()):
            services_data = Service.objects.all()
            context['services_data'] = services_data

        context['gallery_page'] = 'active'
        # context['albums'] = album

        return context
