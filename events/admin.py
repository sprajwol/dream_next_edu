from django.contrib import admin
from django.template.loader import get_template
from django.utils.translation import gettext as _
from django_summernote.admin import SummernoteModelAdmin

from events.models import Event, Category
# Register your models here.


class EventAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)

    list_display = ('title', 'id',)
    prepopulated_fields = {'slug': ('title',)}
    fields = ('title', 'slug', 'main_image', 'image_thumb', 'date', 'category',
              'summary', 'description')

    readonly_fields = ("image_thumb",)

    def image_thumb(self, instance):
        """A (pseudo)field that returns an image thumbnail for a show photo."""
        tpl = get_template("events/admin/image_thumbnail.html")
        return tpl.render({"image": instance.main_image})

    image_thumb.short_description = _("Main Image Preview")


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Event, EventAdmin)
admin.site.register(Category, CategoryAdmin)
