from django.views.generic import TemplateView, ListView, DetailView

from latestnews.models import News
from test_prep.models import Course
# Create your views here.


class LatestNewsView(ListView):
    model = News
    template_name = 'latestnews/latestnews.html'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        if (Course.objects.all().exists()):
            course_data = Course.objects.all()
            context['course_data'] = course_data

        context['latest_news_page'] = 'active'
        return context


class LatestNewsDetailView(DetailView):
    model = News
    template_name = 'latestnews/singlenews.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        if (Course.objects.all().exists()):
            course_data = Course.objects.all()
            context['course_data'] = course_data

        context['latest_news_page'] = 'active'
        return context
