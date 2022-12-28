from rest_framework import viewsets

from pokemon import models
from .serializers import PokemonSerializer


class PokemonViewSet(viewsets.ModelViewSet):
    queryset = models.Pokemon.objects.all()
    serializer_class = PokemonSerializer
