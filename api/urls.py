from django.urls import path
from .views import *

urlpatterns = [
    path('', api_view, name='api_view' ),
]