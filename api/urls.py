from django.urls import path, include
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', apiBase, name='apiBase'),
    path('home/', apiHome, name='apiHome'),
    path('course/<course_id>/', apiSingleCourse, name='apiSingleCourse'),
    path('blog/<blog_id>/', apiSingleBlog, name='apiSingleBlog'),
    path('blogs/', apiBlogs, name='apiBlogs'),
    path('courses/', apiCourses, name='apiCourses'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)