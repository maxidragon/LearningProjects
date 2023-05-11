from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('articles/', views.ListCreateArticle.as_view()),
    path('articles/<int:pk>/', views.ArticleDetail.as_view()),
    path('users/', views.ListCreateUser.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
