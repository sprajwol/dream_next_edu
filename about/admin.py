from django.contrib import admin

from about.models import Testimonial, Member
# Register your models here.


class MemberAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'position', 'email')


admin.site.register(Testimonial)
admin.site.register(Member, MemberAdmin)
