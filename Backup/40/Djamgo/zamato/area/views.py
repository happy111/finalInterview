from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from . serializers import *
from . models import *
# Create your views here.


   
class AreaCreation(CreateAPIView):
    """
    Area Creation POST API
        Service Usage and Description : This API is used to create Area.
            Authentication Required : YES

            Data : {
                "name" : "XYZ"
            }

            Response : {
                "data" : final_data
            }
    """
    serializer_class = GenreSerializer
    def post(self, request):
        try:
            data = request.data
            serializer = GenreSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(
                    {"success": True, "message": "Genre Created."},
                    status=HTTP_201_CREATED
                )
        except Exception as e:
            return Response(
                {"success": False, "message": str(e)},
                status=HTTP_406_NOT_ACCEPTABLE
            )