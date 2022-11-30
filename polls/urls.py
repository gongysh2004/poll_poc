from django.urls import re_path,path,include
from rest_framework.routers import DefaultRouter

from . import views
app_name = 'polls'
router = DefaultRouter()
router.register(r'question', views.QuestionViewSet)
urlpatterns = [
    path('', views.index, name='index'),
    path('mgmt/', include(router.urls), name='mgmt_create'),
    path('create_get/', views.create_get, name='create_get'),
    path('create_post/', views.create_post, name='create_post'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),

]
