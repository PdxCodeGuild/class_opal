from django.urls import path

from .views import PersonalizedIndexViewSet, OrderDownloadView, PersonalizedIndexDownloadView, PersonalizedIndexStatsView, CashFlowPlanView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', PersonalizedIndexViewSet, basename='personalized_index')
urlpatterns = [
    path('download/orders/<str:index_id>/',
         OrderDownloadView.as_view(), name='download-orders'),
    path('download/index/<str:index_id>/',
         PersonalizedIndexDownloadView.as_view(), name='download-index'),
    path('personalizedindexstats/<int:index_id>/',
         PersonalizedIndexStatsView.as_view(), name='personalized_index_stats'),
    path('cash-flow-plan/', CashFlowPlanView.as_view(), name='cash_flow_plan'),
] + router.urls
