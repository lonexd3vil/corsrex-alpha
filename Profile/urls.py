from django.urls import path, include
from .views import *

urlpatterns = [
    path('<str:id>/', profileHome, name='ProfileHome')
]
