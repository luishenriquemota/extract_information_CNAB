from django import views
from django.urls import path
from . import views

urlpatterns = [
    path("upload/", views.UploadView.as_view()),
    path("convert/<str:id_file>/", views.ConvertFileView.as_view())
]