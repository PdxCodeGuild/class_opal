from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results', views.results, name='results'),
    path('<int:question_id>/vote', views.vote, name='vote'),
    path('add_question/', views.add_question, name='add'),
    path('<int:question_id>/choice_page/',
         views.choice_page, name='choice_page'),
    path('<int:question_id>/add_choice/', views.add_choice, name='add_choice'),
]
