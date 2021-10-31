from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from latestnews import views as latest_news_views

urlpatterns = [
    path('', latest_news_views.LatestNewsView.as_view(),
         name='latest_news'),
    path('<slug:slug>', latest_news_views.LatestNewsDetailView.as_view(),
         name='latest_news_detail')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
