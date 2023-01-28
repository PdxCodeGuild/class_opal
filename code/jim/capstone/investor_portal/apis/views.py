import os
import json
from django.http import HttpResponse
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
    def get(self, request, index_id, format=None):
        index = models.PersonalizedIndex.objects.get(id=index_id)
        index_name = index.index_name
        index_allocation = index.index_allocation
        market_cap_min = index.market_cap_min
        dividend_yield_min = index.dividend_yield_min
        pe_ratio_max = index.pe_ratio_max
        sector_exclude_1 = index.sector_exclude_1
        sector_exclude_2 = index.sector_exclude_2
        get_personalized_index(index_name, index_allocation, market_cap_min,
                               dividend_yield_min, pe_ratio_max, sector_exclude_1, sector_exclude_2)
        file_path = os.path.join(os.path.dirname(
            os.path.abspath(__file__)), 'data', f'orders_{index_name}.csv')
        file = open(file_path, 'rb')
        response = HttpResponse(file, content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="orders_{index_name}.csv"'
        return response


class PersonalizedIndexDownloadView(APIView):
    def get(self, request, index_id, format=None):
        index = models.PersonalizedIndex.objects.get(id=index_id)
        index_name = index.index_name
        index_allocation = index.index_allocation
        market_cap_min = index.market_cap_min
        dividend_yield_min = index.dividend_yield_min
        pe_ratio_max = index.pe_ratio_max
        sector_exclude_1 = index.sector_exclude_1
        sector_exclude_2 = index.sector_exclude_2
        get_personalized_index(index_name, index_allocation, market_cap_min,
                               dividend_yield_min, pe_ratio_max, sector_exclude_1, sector_exclude_2)
        file_path = os.path.join(os.path.dirname(
            os.path.abspath(__file__)), 'data', f'personalized_index_{index_name}.csv')
        file = open(file_path, 'rb')
        response = HttpResponse(file, content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="personalized_index_{index_name}.csv"'
        return response
