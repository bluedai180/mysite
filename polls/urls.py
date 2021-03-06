from django.urls import path, re_path

from . import views

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('test', views.test, name='test'),
    path('add/', views.add, name='add'),
    path('ajax_dict/', views.ajax_dict, name='ajax_dict')
    # re_path(r'^add/$', views.add, name='add')
]
