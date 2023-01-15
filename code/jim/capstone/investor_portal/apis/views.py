from rest_framework import viewsets

from personalized_index import models
from .serializers import PersonalizedIndexSerializer


class PersonalizedIndexViewSet(viewsets.ModelViewSet):
    queryset = models.PersonalizedIndex.objects.all()
    serializer_class = PersonalizedIndexSerializer
