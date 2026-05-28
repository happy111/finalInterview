from django.shortcuts import render
from rest_framework.generics import(
        CreateAPIView,
        ListAPIView,
        UpdateAPIView,
        )

from .serializers import AreaSerializer
from rest_framework.permissions import IsAuthenticated

from win.permissions import (
                                        IsShopOwner, 
                                        IsNotBanned , 
                                        IsSuperAdmin)

from rest_framework import generics, mixins
from . models import *

# from userrole.permissions import IsSuperAdmin, IsAdmin
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_406_NOT_ACCEPTABLE





class AreaUpdation(UpdateAPIView):
    """
    Area Updation PUT API

            Service Usage and Description : This API is used to update Area.
            Authentication Required : YES

            Data : {
                "id" : "1",
                "name": "ABC"
            }

            Response : {
                "success": True,
                "message": "Area Updated."
            }
    """

    # permission_classes = (IsAuthenticated, IsSuperAdmin | IsAdmin)
    serializer_class = AreaSerializer
    def put(self,request):
        try:
            data = request.data 
            area = Area.objects.filter(id=data['id'])
            if area.count() == 0:
                raise Exception("No Area with given id.")
            serializer = AreaSerializer(area[0], data=data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(
                    {"success": True, "message":"Area Updated."},
                    status=HTTP_200_OK,)
        except Exception as e:
            return Response(
                 {"success": False, "message": str(e)},
                 status=HTTP_406_NOT_ACCEPTABLE
                )























class ActiveAreaStateCity(ListAPIView):
    """
    All Area/State/City Listing GET API

        Service Usage and Description : This API is used to list all Area/State/City.
        Authentication Required : YES

        Params : {
     
        }

        Response : {
            "data" : final_data
        }
    """

    # permission_classes = (IsAuthenticated,)
    # serializer_class = AreaSerializer
    def get_queryset(self):
        queryset = Area.objects.filter(active_status=1).order_by('priority')
        return queryset
    def get(self,request):
        try:
            queryset = self.get_queryset()
            finaldata = []
            for index in queryset:
                    area_dict = {}
                    area_dict["id"] = index.id 
                    area_dict["area"] = index.name
                    state_data = State.objects.filter(active_status=1,area_id=index.id)
                    area_dict["state"] = []
                    if state_data.count() > 0:
                            state = {}
                            for s in state_data:
                                    state['name'] = s.name
                                    state['id'] = s.id 
                                    state['area_id'] = s.area_id
                                    area_dict["state"].append(state)
                                    city_data = City.objects.filter(active_status=1,state_id=s.id)
                                    if city_data.count() > 0:
                                        state['city'] = []
                                        for c in city_data:
                                            city = {}
                                            city['city_id'] = c.id
                                            city['name'] = c.name
                                            state['city'].append(city)
                                    else:
                                        pass
                    else:
                            pass 

                    finaldata.append(area_dict)
            return Response(finaldata, status=HTTP_200_OK) 


        except Exception as e:
                return Response(
                                {
                                    "success": False, 
                                    "message": str(e)}, 
                                     status=HTTP_406_NOT_ACCEPTABLE
                        )












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

    permission_classes = (IsAuthenticated,)
    serializer_class = AreaSerializer



class ActiveAreaListing(mixins.ListModelMixin,generics.GenericAPIView):
        queryset = Area.objects.all()
        serializer_class = AreaSerializer

        def get(self, request, *args, **kwargs):
                return self.list(request, *args, **kwargs)
