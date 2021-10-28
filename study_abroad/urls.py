from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from study_abroad import views as study_abroad_views

urlpatterns = [
    path('', study_abroad_views.StudyAbroadView.as_view(),
         name='study_abroad'),
    path('<slug:slug>', study_abroad_views.SingleCountryView.as_view(),
         name='single_country'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
