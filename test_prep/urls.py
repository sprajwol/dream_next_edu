from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from test_prep import views as test_prep_views

urlpatterns = [
    path('', test_prep_views.TestPreparationView.as_view(),
         name='test_preparation'),
    path('<slug:slug>', test_prep_views.TestPreparationDetailView.as_view(),
         name='test_prep_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
