from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('start/', views.start_quiz, name='start_quiz'),
    path('quiz/', views.quiz, name='quiz'),
    path('save-answer/', views.save_answer, name='save_answer'),
    path('submit/', views.submit_quiz, name='submit_quiz'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
]