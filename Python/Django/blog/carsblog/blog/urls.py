from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:postId>/', views.detail, name='detail')
    ]

