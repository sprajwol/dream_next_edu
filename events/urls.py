from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from events import views as events_views

urlpatterns = [
    path('', events_views.EventView.as_view(), name='events'),
    path('<slug:slug>', events_views.EventDetailView.as_view(),
         name='eventdetail')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
