from rest_framework import viewsets
from rest_framework.generics import RetrieveUpdateDestroyAPIView
# from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from pokemon import models
from .serializers import PokemonSerializer


class PokemonViewSet(viewsets.ModelViewSet):
    queryset = models.Pokemon.objects.all()
    serializer_class = PokemonSerializer
    # csrf_exempt = True

    def perform_create(self, serializer):
        serializer.save()


class RetrieveUpdateDestroyPokemonAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = PokemonSerializer
    queryset = models.Pokemon.objects.all()
    # csrf_exempt = True

# class PokemonCreateView(generics.CreateAPIView):
#     queryset = models.Pokemon.objects.all()
#     serializer_class = PokemonSerializer
#     csrf_exempt = True

#     def create_pokemon(self, request):
#         if request.method == 'POST':
#             # Deserialize the request data
#             serializer = PokemonSerializer(data=request.data)
#             if serializer.is_valid():
#                 # Create a new Pokemon instance from the validated data
#                 pokemon = serializer.save()
#                 # Return a JSON response with the serialized Pokemon data
#                 return Response(serializer.data)
#             else:
#                 # Return an error response if the data is invalid
#                 return Response({'error': serializer.errors}, status=400)
