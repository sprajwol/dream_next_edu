from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from gallery import views as gallery_views

urlpatterns = [
    path('', gallery_views.GalleryView.as_view(), name='gallery'),
    path('<slug:photo_album_name_slug>',
         gallery_views.AlbumView.as_view(), name='album')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
