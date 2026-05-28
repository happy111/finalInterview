from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from common.models import Common

class Genre(Common):
    name = models.CharField(
        max_length=100, 
        unique=True, 
        verbose_name="Genre Name")
    priority = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        default=10,
        verbose_name="List priority of the Genre",
    )

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"

    def __str__(self):
        return self.name
