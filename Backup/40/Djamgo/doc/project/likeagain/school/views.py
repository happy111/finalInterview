from django.shortcuts import render
from rest_framework.generics import(
      CreateAPIView,
      ListAPIView
)
from .serializers import *
# Create your views here.

class TeacherCreation(CreateAPIView):
