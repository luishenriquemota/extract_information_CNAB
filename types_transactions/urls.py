from django.urls import path
from . import views

urlpatterns = [
    path("types/", views.TypesView.as_view()),
]