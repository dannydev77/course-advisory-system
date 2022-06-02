from django.contrib import admin
from .models import School, Course, Advice, Application


# Register your models here.
admin.site.register(School)
admin.site.register(Course)
admin.site.register(Advice)
admin.site.register(Application)

admin.site.site_header = 'Student Course Advisory Administration'
admin.site.site_title = 'Iyvone'
admin.site.index_title = 'Welcome to Iyvone Adminstration'