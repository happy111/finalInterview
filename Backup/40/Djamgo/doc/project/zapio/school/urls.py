from django.urls import path
from .views import *

urlpatterns = [
    path("teacher/", TeacherCreate.as_view()),
    path("teacher/", TeacherUpdate.as_view()),

]