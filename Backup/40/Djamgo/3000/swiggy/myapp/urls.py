from django.urls import path
from .views import UserCreateView, UserDetailView

urlpatterns = [
    path('create/', UserCreateView.as_view(), name='user-create'),
    path('user/<int:user_id>/', UserDetailView.as_view(), name='user-detail'),
]
