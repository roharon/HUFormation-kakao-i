from django.urls import path
import views
urlpatterns = [
    path('^keyboard/',views.keyboard)
]