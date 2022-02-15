from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from home import views as home_views
from contact import views as contact_views

urlpatterns = [
    path('', home_views.HomeView.as_view(), name='home'),
    path('enquiry', contact_views.EnquiryView.as_view(), name='enquiry')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
