from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('project', views.project, name="project"),
    path('about', views.about, name="about"),
    path('result', views.output, name="output")
]