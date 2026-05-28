from django.shortcuts import render
from rest_framework.generics import(
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
    ListAPIView
)
from .serializers import *
from rest_framework.status import (
    HTTP_200_OK, 
    HTTP_406_NOT_ACCEPTABLE)
from rest_framework.response import Response



# Create your views here.

class GenreCreation(CreateAPIView):
    """
    Genre Creation POST API

    	Service Usage and Description : This API is used to create Genre.
	    Authentication Required : YES

	    Data : {
	        "name" : "XYZ"
	    }

	    Response : {
	        "data" : final_data
	    }
    """

    #permission_classes = (IsAuthenticated, IsSuperAdmin | IsAdmin)
    serializer_class = GenreSerializer

class GenreUpdation(UpdateAPIView):
    """
    Genre Updation PUT API

	    Service Usage and Description : This API is used to update Genre.
	    Authentication Required : YES

	    Data : {
	        "id" : "1",
	        "name": "ABC"
	    }

	    Response : {
	        "success": True,
	        "message": "Genre Updated."
	    }
    """
    serializer_class = GenreSerializer
    def put(self,request):
        try:
            data = request.data 
            genre_data = Genre.objects.filter(id=data['id'])
            if genre_data.count() == 0:
                raise Exception("No Genre with given id.")
            serializer = GenreSerializer(genre_data[0],data=data,partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(
                    {"success": True, "message": "Genre Updated."}, status=HTTP_200_OK,
                )
        except Exception as e:
            return Response(
                    {"success" : False, 'message' : str(e) },
                            status=HTTP_406_NOT_ACCEPTABLE,)


class GenreDeletion(DestroyAPIView):
    """
    Genre Deletion DELETE API

	    Service Usage and Description : This API is used to delete Genre.
	    Authentication Required : YES

	    Data : {
	        "id" : "1"
	    }
	    
	    Response : {
            "success": True,
            "message": "Genre Deleted."
        }
    """
    # permission_classes = (IsAuthenticated, IsSuperAdmin | IsAdmin)
    serializer_class = GenreSerializer

    def get_queryset(self):
        genre_id = self.request.data['id']
        queryset = Genre.objects.filter(id=genre_id)
        return queryset
    def delete(self, request):
        try:
            genre = self.get_queryset()
            if genre.count() == 0:
                raise Exception("No Genre with given id.")
            self.perform_destroy(genre)
            return Response(
                {"success": True, "message": "Genre Deleted."}, status=HTTP_200_OK,
            )
        except Exception as e:
            return Response(
                {"success": False, "message": str(e)}, status=HTTP_406_NOT_ACCEPTABLE
            )
        
class ActiveGenreListing(ListAPIView):
    """
    Active Genre Listing GET API

	    Service Usage and Description : This API is used to list active Genres.
	    Authentication Required : YES

	    Response : {
	        "data" : final_data
	    }
        
    """
    serializer_class = GenreSerializer

    def get_queryset(self):
        queryset = Genre.objects.filter(active_status=True)
        return queryset
