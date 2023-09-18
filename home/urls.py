from django.urls import path, include
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', homeBase, name='homeBase')
]