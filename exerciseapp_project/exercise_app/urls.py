from django.urls import path
from . import views

urlpatterns = [
    # need to chnage end points and add stretches and cues
path('', views.ListExercises.as_view()),

]