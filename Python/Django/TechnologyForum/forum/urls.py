from . import views
from django.urls import path

app_name = 'forum'

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('questions/', views.questions, name='questions'),
    path('detail/<int:questionId>', views.detail, name='detail'),
    path('answer/', views.addAnswer, name='answer'),
    path('like/<int:questionId>', views.like, name='like'),
    path('likeAnswer/<int:answerId>', views.likeAnswer, name='likeAnswer'),
    path('edit/<int:questionId>', views.edit, name='edit'),
    path('editAnswer/<int:answerId>', views.editAnswer, name='editAnswer'),
    path('deleteAnswer/<int:answerId>', views.deleteAnswer, name='deleteAnswer'),
    path('delete/<int:questionId>', views.delete, name='delete'),
    path('questions/my/', views.myQuestions, name='myQuestions'),
    ]