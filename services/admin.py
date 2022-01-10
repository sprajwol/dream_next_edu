from django.contrib import admin
from django.template.loader import get_template
from django.utils.translation import gettext as _
from django_summernote.admin import SummernoteModelAdmin

from services.models import Service, Scholoarship
# Register your models here.


class ServiceAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)

    list_display = ('title', 'id',)
    prepopulated_fields = {'slug': ('title',)}
    fields = ('title', 'slug', 'main_image',
              'image_thumb', 'summary', 'description')

    readonly_fields = ("image_thumb",)

    def image_thumb(self, instance):
        """A (pseudo)field that returns an image thumbnail for a show photo."""
        tpl = get_template("events/admin/image_thumbnail.html")
        return tpl.render({"image": instance.main_image})

    image_thumb.short_description = _("Main Image Preview")

class ScholoarshipAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)

    list_display = ('title', 'id',)
    prepopulated_fields = {'slug': ('title',)}
    fields = ('title', 'slug', 'main_image',
              'image_thumb', 'summary', 'description')

    readonly_fields = ("image_thumb",)

    def image_thumb(self, instance):
        """A (pseudo)field that returns an image thumbnail for a show photo."""
        tpl = get_template("events/admin/image_thumbnail.html")
        return tpl.render({"image": instance.main_image})

    image_thumb.short_description = _("Main Image Preview")


admin.site.register(Service, ServiceAdmin)
admin.site.register(Scholoarship, ScholoarshipAdmin)
