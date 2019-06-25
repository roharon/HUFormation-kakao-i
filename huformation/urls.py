from django.urls import path
from huformation import views

urlpatterns = [
    path('apiTest/', views.apiTest),
    path('skill', views.skill)
]