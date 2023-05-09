from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('tasks/', views.tasks, name='tasks'),
    path('create/', views.create, name='create'),
    path('delete/<int:taskId>', views.delete, name='delete'),
    path('complete/<int:taskId>', views.complete, name='complete'),
    path('tasks/<int:taskId>/', views.detail, name='detail')
]
