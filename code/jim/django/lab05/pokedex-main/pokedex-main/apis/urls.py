from django.urls import path

from .views import PokemonViewSet, RetrieveUpdateDestroyPokemonAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', PokemonViewSet, basename='pokemon')
# router.register('', RetrieveUpdateDestroyPokemonAPIView, basename='pokemon')
# Add the view to the URL patterns
urlpatterns = [
    path('pokemon/<int:pk>/',
         RetrieveUpdateDestroyPokemonAPIView.as_view(), name='pokemon-detail'),
]
# Add the router's URL patterns to the list
urlpatterns += router.urls
