from django.urls import path
from .views import threaded_purchase_view

urlpatterns = [
    path('buy-threaded/<int:product_id>/', threaded_purchase_view, name='threaded-purchase'),
]
