import os
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from django.http import FileResponse

from personalized_index import models
from .pers_index_maker import get_personalized_index
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


class OrderDownloadView(APIView):
    def get(self, request, index_name, format=None):
        file_path = os.path.join(os.path.dirname(
            os.path.abspath(__file__)), 'data', f'orders_{index_name}.csv')
        response = FileResponse(open(file_path, 'rb'))
        response['Content-Disposition'] = f'attachment; filename="orders_{index_name}.csv"'
        return response
