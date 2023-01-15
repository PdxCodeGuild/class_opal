from django.urls import path

from .views import PersonalizedIndexViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', PersonalizedIndexViewSet, basename='personalized_index')
urlpatterns = router.urls
