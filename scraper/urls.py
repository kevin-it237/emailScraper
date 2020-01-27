from django.urls import path, include
from . import views

urlpatterns = [
    path('find', views.FindEmailsView.as_view()),
]