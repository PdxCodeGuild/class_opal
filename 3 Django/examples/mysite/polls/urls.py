from django.urls import path
from django.views.generic.base import TemplateView

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote', views.vote, name='vote'),
    path('add_question/', views.add_question, name='add'),
    path('<int:question_id>/choice_page/',
         views.choice_page, name='choice_page'),
    path('<int:question_id>/add_choice/', views.add_choice, name='add_choice'),
    path('fake-page/', TemplateView.as_view(template_name='fake'), name='fake')
]
