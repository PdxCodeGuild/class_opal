from django.urls import path

from .views import PersonalizedIndexViewSet, OrderDownloadView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', PersonalizedIndexViewSet, basename='personalized_index')
urlpatterns = [
    path('download/orders/<str:index_name>/',
         OrderDownloadView.as_view(), name='download-orders'),
] + router.urls
