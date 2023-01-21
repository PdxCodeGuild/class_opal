from django.urls import path

from .views import PersonalizedIndexViewSet, OrderDownloadView, PersonalizedIndexDownloadView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', PersonalizedIndexViewSet, basename='personalized_index')
urlpatterns = [
    path('download/orders/<str:index_id>/',
         OrderDownloadView.as_view(), name='download-orders'),
    path('download/index/<str:index_id>/',
         PersonalizedIndexDownloadView.as_view(), name='download-index'),
] + router.urls
