from django.contrib import admin
from django.template.loader import get_template
from django.utils.translation import gettext as _

from gallery.models import Album, Image
from gallery.forms import AlbumAdminForm
# Register your models here.


class ImageInline(admin.TabularInline):
    model = Image

    fields = ("showphoto_thumbnail",)
    readonly_fields = ("showphoto_thumbnail",)
    max_num = 0

    def showphoto_thumbnail(self, instance):
        """A (pseudo)field that returns an image thumbnail for a show photo."""
        tpl = get_template("gallery/admin/show_thumbnail.html")
        return tpl.render({"image": instance.image})

    showphoto_thumbnail.short_description = _("Thumbnail")


class AlbumAdmin(admin.ModelAdmin):
    form = AlbumAdminForm
    list_display = ['photo_album_name']
    inlines = [ImageInline]
    prepopulated_fields = {'photo_album_name_slug': ('photo_album_name',)}

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        form.save_photos(form.instance)


admin.site.register(Album, AlbumAdmin)
