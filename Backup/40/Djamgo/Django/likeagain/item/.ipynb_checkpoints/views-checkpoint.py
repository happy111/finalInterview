from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Item
from .serializers import ItemSerializer
from django.core.cache import cache
from django.shortcuts import get_object_or_404

class ItemListCreateAPIView(APIView):
    @swagger_auto_schema(
        operation_description="Get a list of items or create a new item.",
        responses={
            200: ItemSerializer(many=True),
            201: ItemSerializer,
            400: 'Bad Request',
        }
    )
    def get(self, request):
        cached_items = cache.get('items_list')
        if cached_items:
            return Response(cached_items)
        
        items = Item.objects.all()
        breakpoint()
        serializer = ItemSerializer(items, many=True)
        cache.set('items_list', serializer.data, timeout=60*5)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Create a new item.",
        request_body=ItemSerializer,
        responses={201: ItemSerializer, 400: 'Bad Request'}
    )
    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            item = serializer.save()
            cache.set(f'item_{item.id}', serializer.data, timeout=60*5)
            cache.delete('items_list')
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ItemDetailAPIView(APIView):
    @swagger_auto_schema(
        operation_description="Get details of an individual item.",
        responses={200: ItemSerializer, 404: 'Item not found'}
    )
    def get(self, request, pk):
        cached_item = cache.get(f'item_{pk}')
        if cached_item:
            return Response(cached_item)
        
        item = get_object_or_404(Item, pk=pk)
        serializer = ItemSerializer(item)
        cache.set(f'item_{item.id}', serializer.data, timeout=60*5)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Update an existing item.",
        request_body=ItemSerializer,
        responses={200: ItemSerializer, 400: 'Bad Request', 404: 'Item not found'}
    )
    def put(self, request, pk):
        item = get_object_or_404(Item, pk=pk)
        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            item = serializer.save()
            cache.set(f'item_{item.id}', serializer.data, timeout=60*5)
            cache.delete('items_list')
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Delete an existing item.",
        responses={204: 'No Content', 404: 'Item not found'}
    )
    def delete(self, request, pk):
        item = get_object_or_404(Item, pk=pk)
        item.delete()
        cache.delete(f'item_{pk}')
        cache.delete('items_list')
        return Response(status=status.HTTP_204_NO_CONTENT)
