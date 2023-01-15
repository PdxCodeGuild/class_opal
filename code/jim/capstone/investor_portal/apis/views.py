from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render

from personalized_index import models
from .serializers import PersonalizedIndexSerializer


class PersonalizedIndexViewSet(viewsets.ModelViewSet):
    queryset = models.PersonalizedIndex.objects.all()
    serializer_class = PersonalizedIndexSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        context = {}
        context["user_id"] = self.request.user.id
        return render(request, 'your_template.html', context)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
