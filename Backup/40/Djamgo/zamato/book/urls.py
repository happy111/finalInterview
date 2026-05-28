
from django.urls import path
from .views import *


urlpatterns = [
    path('create/', BookCreateAPIView.as_view(), name='book-create'),
    path('list/', BookListAPIView.as_view(), name='book-list')  # ✅ new GET API


]