from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from genre.models import Genre
from area.models import Area,City


class Shop(models.Model):
    genre = models.ForeignKey(
        Genre,
        related_name="shop_genre",
        on_delete=models.CASCADE,
        verbose_name="Shop Genre",
    )
    name = models.CharField(
        max_length=100, 
        verbose_name="Shop Name",
        unique=True)

    city = models.ForeignKey(
        City,
        related_name="shop_city",
        on_delete=models.CASCADE,
        verbose_name="Shop City",
    )
    url = models.CharField(
        max_length=100, 
        verbose_name="Url",
        null=True,
        blank=True,
        )
    address = models.CharField(
        max_length=250, 
        null=True, 
        blank=True, 
        verbose_name="Shop Address"
    )
    profile_photo = models.ImageField(
        upload_to="shops/", 
        null=True, 
        blank=True, 
        verbose_name="Shop Profile Photo"
    )
    banner = models.ImageField(
        upload_to="shops/", 
        null=True, 
        blank=True, 
        verbose_name="Shop Banner Photo"
    )
    bio = models.CharField(
        max_length=500, 
        null=True, 
        blank=True, 
        verbose_name="Shop Bio"
    )
    opening_time = models.TimeField(
        auto_now=False,
        auto_now_add=False,
        null=True,
        blank=True,
        verbose_name="Shop Opening Time",
    )
    closing_time = models.TimeField(
        auto_now=False,
        auto_now_add=False,
        null=True,
        blank=True,
        verbose_name="Shop Closing Time",
    )
    is_24hr_open = models.BooleanField(
        default=False, 
        null=True, 
        blank=True, 
        verbose_name="Is Shop 24hr Open"
    )

    phone_number = models.CharField(
        max_length=20,
        verbose_name='Mobile No',
        null=True,
        blank=True)

    comment = models.CharField(
        max_length=20,
        verbose_name='Comment',
        null=True,
        blank=True)

    staff_attitude_rating = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        null=True,
        blank=True,
        verbose_name="Shop Staff Attitude Rating",
    )
    pay_rating = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        null=True,
        blank=True,
        verbose_name="Shop Pay Rating",
    )
    user_rating = models.FloatField(
        default=0.0,
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        null=True,
        blank=True,
        verbose_name="Shop User Rating",
    )
    review_count = models.PositiveIntegerField(
        null=True, 
        blank=True, 
        verbose_name="Review Count"
    )
    views_count = models.PositiveIntegerField(
        default=0, 
        null=True, 
        blank=True, 
        verbose_name="View Count"
    )
    is_premium = models.BooleanField(
        default=0, 
        null=True, 
        blank=True, 
        verbose_name="Is Premium Member"
    )
    is_banned = models.BooleanField(
        default=0, 
        null=True, 
        blank=True, 
        verbose_name="Is Shop Banned"
    )

    class Meta:
        verbose_name = "Shop"
        verbose_name_plural = "Shops"

    def __str__(self):
        return self.name


class FAQ(models.Model):
    shop = models.ForeignKey(
        Shop, 
        on_delete=models.CASCADE, 
        related_name="faq_shop", 
        verbose_name="Shop"
    )
    question = models.CharField(
    	max_length=500, 
    	verbose_name="Question")
    answer = models.CharField(
    	max_length=500, 
    	verbose_name="Answer")


    class Meta:
        verbose_name = "FAQ for Shop"
        verbose_name_plural = "FAQ for shops"

    def __str__(self):
        return self.shop.name

