from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'srsran', srsranModelViewSet)

urlpatterns = [
    path('', api_view, name='api_view' ),
    path('api/', include(router.urls)),
    path('ejecutar-scripts/', EjecutarScriptsView.as_view(), name='ejecutar-scripts'),
]