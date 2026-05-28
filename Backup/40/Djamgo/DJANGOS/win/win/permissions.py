from rest_framework import permissions
from users.models import *
from rest_framework.permissions import DjangoModelPermissions

class IsShopOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        try:
            shopowner = ShopOwner.objects.filter(auth_user=user)
            if shopowner.count():
                return True
        except Exception as e:
            return False


class IsNotBanned(permissions.BasePermission):
    def has_permission(self, request, view):
        auth_user = request.user.id
        try:
            enduser = EndUser.objects.filter(auth_user=auth_user).first()
            return not (enduser.is_banned)
        except Exception as e:
            return False


class IsPremiumShop(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        try:
            shopowner = ShopOwner.objects.filter(auth_user=user)
            if shopowner.count():
                shopowner = shopowner.first()
                return shopowner.shop.is_premium
        except Exception as e:
            return False

class IsSuperAdmin(DjangoModelPermissions):
    def has_permission(self, request, view):
        user = request.user
        return user.is_superuser