from django.db import models
from django.contrib.auth.models import User
from shops.models import Shop
from area.models import Area


class ShopOwner(models.Model):
    shop = models.ForeignKey(
        Shop,
        related_name="shopowner_shop",
        on_delete=models.CASCADE,
        verbose_name="Shop",
    )
    auth_user = models.OneToOneField(
        User,
        related_name="shopowner_auth_user",
        on_delete=models.CASCADE,
        verbose_name="Shop Owner",
    )
    name = models.CharField(
    	max_length=100, 
    	verbose_name="Shop Owner Name")
    
    email = models.CharField(
        max_length=100, 
        null=True, 
        blank=True, 
        verbose_name="Shop Owner Email"
    )
    photo = models.ImageField(
        upload_to="users/", 
        null=True, 
        blank=True, 
        verbose_name="Profile Picture"
    )
    active_status = models.BooleanField(
        default=1, 
        null=True, 
        blank=True, 
        verbose_name="Shop Owner Active Status"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        null=True,
        blank=True,
        verbose_name="Creation Date & Time",
    )
    updated_at = models.DateTimeField(
        auto_now=True, 
        null=True, 
        blank=True, 
        verbose_name="Updation Date & Time"
    )

    class Meta:
        verbose_name = "Shop Owner"
        verbose_name_plural = "Shop Owners"

    def __str__(self):
        return self.name


class EndUser(models.Model):
    auth_user = models.OneToOneField(
        User,
        related_name="enduser_auth_user",
        on_delete=models.CASCADE,
        verbose_name="Auth User",
    )

    area = models.ForeignKey(
        Area,
        null=True, 
        blank=True, 
        related_name="enduser_area",
        on_delete=models.CASCADE,
        verbose_name="Area",
    )
    name = models.CharField(
            max_length=100, 
            null=True, 
            blank=True, 
            verbose_name="Display Name")
    avatar = models.URLField(
        max_length=200, 
        null=True, 
        blank=True, 
        verbose_name="End User Avatar"
    )
    age = models.PositiveIntegerField(
        null=True, 
        blank=True, 
        verbose_name="End User Age"
    )
    is_banned = models.BooleanField(
        default=0, 
        null=True, 
        blank=True, 
        verbose_name="Is end user banned ?"
    )
    active_status = models.BooleanField(
        default=1, 
        null=True, 
        blank=True, 
        verbose_name="End User Active Status"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        null=True,
        blank=True,
        verbose_name="Creation Date & Time",
    )
    updated_at = models.DateTimeField(
        auto_now=True, 
        null=True, 
        blank=True, 
        verbose_name="Updation Date & Time"
    )

    description = models.CharField(
        max_length=1000, 
        null=True, 
        blank=True, 
        verbose_name="Description")

    views_count = models.PositiveIntegerField(
        default=0, 
        null=True, 
        blank=True, 
        verbose_name="View Count"
    )

    class Meta:
        verbose_name = "End User"
        verbose_name_plural = "End Users"

    def __str__(self):
        return self.name
