from django.contrib import admin
from .models import *
from Profile.models import *
# Register your models here.

admin.site.register(Instructer),
admin.site.register(CourseCategory),
admin.site.register(Courses),
admin.site.register(CourseIncludes),
admin.site.register(HomeModel),
admin.site.register(Blog),
admin.site.register(CustomUser)