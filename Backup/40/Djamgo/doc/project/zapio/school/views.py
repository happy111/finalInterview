from django.shortcuts import render
from rest_framework.generics import(
            CreateAPIView,
            ListAPIView,
            UpdateAPIView
)

from .serializers import TeacherSerializer
from .models import *
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK,HTTP_406_NOT_ACCEPTABLE
# Create your views here.
class TeacherCreate(CreateAPIView):
    serializer_class = TeacherSerializer

class TeacherUpdate(UpdateAPIView):
    serializer_class = TeacherSerializer
    def put(self,request, *args, **kwargs):
        try:
            data = request.data
            teacher_data = Teacher.objects.filter(id=data['id'])
            if teacher_data.count() == 0:
                raise Exception("No teacher with given id")
            serializer = TeacherSerializer(teacher_data[0],data=data,partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(
                    {
                        "success" : True,
                        "message" : "Teacher Updated",
                        "status"  : HTTP_200_OK
                    }
                )
        except Exception as e:
            return(
                {
                    "success" : False,
                    "message" : str(e),
                    "status"  : HTTP_406_NOT_ACCEPTABLE
                }
            )

