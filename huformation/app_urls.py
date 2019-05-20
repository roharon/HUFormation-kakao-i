from django.urls import path
from huformation.views import show_test
urlpatterns = [
    path('show_test/', show_test)
]