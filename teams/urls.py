from django.urls import path
from .views import TeamView, TeamParamView;

urlpatterns = [
    path('teams/', TeamView.as_view()),
    path('teams/<int:pk>/', TeamParamView.as_view()),
]