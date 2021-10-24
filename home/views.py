from django.views.generic import TemplateView

from home.models import HeroSlider
# Create your views here.


class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        hero_sliders = HeroSlider.objects.all()

        context['hero_sliders'] = hero_sliders
        context['home_page'] = 'active'
        return context
