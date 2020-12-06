from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<id>', views.take_quiz, name='take_quiz'),
    path('api/<id>', views.api_question, name='api_question'),
]
