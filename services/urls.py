from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from services import views as services_views

urlpatterns = [
    path('', services_views.ServicesListView.as_view(),
         name='services'),
    path('<slug:slug>', services_views.ServicesDetailView.as_view(),
         name='services_detail'),
    path('scholarships', services_views.ServicesListView.as_view(),
         name='scholarships'),
    path('scholarships/<slug:slug>', services_views.ScholarshipsDetailView.as_view(),
         name='scholarships_detail'),

#     path('visa_application', services_views.ServicesVisaListView.as_view(),
#          name='services_visa'),
#     path('visa_application/<slug:slug>', services_views.ServicesVisaDetailView.as_view(),
#          name='services_visa_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
