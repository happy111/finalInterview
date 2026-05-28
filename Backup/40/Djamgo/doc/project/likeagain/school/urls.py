from django.urls import path
from .views import  *

urlpatterns = [

    path('student/',TeacherCreation.as_views()),

]

