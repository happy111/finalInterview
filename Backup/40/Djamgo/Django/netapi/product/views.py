from django.shortcuts import render
from .models import Category
from .serializers import CategorySerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_406_NOT_ACCEPTABLE
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    DestroyAPIView,
    UpdateAPIView,
)
# Create your views here.

class CategoryListing(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryCreation(CreateAPIView):
    def post(self,request):
        data = request.data
        serializer = CategorySerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                {"message":"Category created successfully",
                 "data":serializer.data},
                 status=HTTP_200_OK)
        else:
            return Response(
                {"message":"Category creation failed",
                 "errors":serializer.errors},
                 status=400)