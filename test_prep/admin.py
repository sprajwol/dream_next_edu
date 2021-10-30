from django.contrib import admin
from django.template.loader import get_template
from django.utils.translation import gettext as _
from django_summernote.admin import SummernoteModelAdmin

from test_prep.models import Course
# Register your models here.


class CourseAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)

    list_display = ('name', 'id',)
    prepopulated_fields = {'slug': ('name',)}
    fields = ('name', 'slug', 'main_image',
              'image_thumb')

    readonly_fields = ("image_thumb",)

    def image_thumb(self, instance):
        """A (pseudo)field that returns an image thumbnail for a show photo."""
        tpl = get_template("events/admin/image_thumbnail.html")
        return tpl.render({"image": instance.main_image})

    image_thumb.short_description = _("Main Image Preview")


admin.site.register(Course, CourseAdmin)
