from django.urls import path

from .views import PokemonViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', PokemonViewSet, basename='pokemon')
urlpatterns = router.urls
