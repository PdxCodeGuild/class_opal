import os
import json
from pathlib import Path
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
from .serializers import PersonalizedIndexSerializer, PersonalizedIndexStockSerializer, CashFlowPlanSerializer
from .cash_flow import get_cash_flow


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
        get_personalized_index(index_id)

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
        get_personalized_index(index_id)

        file_path = os.path.join(os.path.dirname(
            os.path.abspath(__file__)), 'data', f'personalized_index_{index_name}.csv')
        file = open(file_path, 'rb')
        response = HttpResponse(file, content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="personalized_index_{index_name}.csv"'
        return response


class PersonalizedIndexStatsView(APIView):
    def get(self, request, index_id, format=None):
        get_personalized_index(index_id)
        stocks = models.PersonalizedIndexStock.objects.filter(
            personalized_index_id=index_id)
        serializer = PersonalizedIndexStockSerializer(stocks, many=True)
        return Response(serializer.data)


class CashFlowPlanView(APIView):
    def get(self, request):
        dob = request.query_params.get('dob', None)
        earned_income = float(request.query_params.get('earned_income', None))
        age_stop = int(request.query_params.get('age_stop', None))
        has_spouse = request.query_params.get('has_spouse', None)
        spouse_dob = request.query_params.get('spouse_dob', None)
        spouse_earned_income = float(request.query_params.get(
            'spouse_earned_income', None))
        spouse_age_stop = int(
            request.query_params.get('spouse_age_stop', None))
        investable_assets = float(
            request.query_params.get('investable_assets', None))
        portfolio_income = float(
            request.query_params.get('portfolio_income', None))
        other_income = float(request.query_params.get('other_income', None))
        transitionary_phase = request.query_params.get(
            'transitionary_phase', None)
        transitionary_length = int(request.query_params.get(
            'transitionary_length', None))
        transitionary_income = float(request.query_params.get(
            'transitionary_income', None))
        retirement_income = float(
            request.query_params.get('retirement_income', None))
        assets_sell = request.query_params.get('assets_sell', None)
        assets_sell_value = float(
            request.query_params.get('assets_sell_value', None))
        assets_buy = request.query_params.get('assets_buy', None)
        assets_buy_value = float(
            request.query_params.get('assets_buy_value', None))
        annual_expenses = float(
            request.query_params.get('annual_expenses', None))
        retirement_lifestyle = request.query_params.get(
            'retirement_lifestyle', None)
        long_term_care_include = request.query_params.get(
            'long_term_care_include', None)
        potential_returns = float(
            request.query_params.get('potential_returns', None))
        get_cash_flow(dob, earned_income, age_stop, has_spouse, spouse_dob, spouse_earned_income, spouse_age_stop, investable_assets, portfolio_income, other_income, transitionary_phase, transitionary_length,
                      transitionary_income, retirement_income, assets_sell, assets_sell_value, assets_buy, assets_buy_value, annual_expenses, retirement_lifestyle, long_term_care_include, potential_returns)
        filepath = Path(__file__).parent / "data"
        with open(filepath / "cash_flow_chart.svg", "rb") as f:
            chart_data = f.read()
        # serializer = CashFlowPlanSerializer(cash_flow_chart)
        return Response(chart_data, content_type="image/png")
