from django.db import models
from common.models import Common
# Create your models here.


class Area(Common):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Area Name")
    priority = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name='Priority')

    class Meta:
        verbose_name = "Area"
        verbose_name_plural = "Areas"

    def __str__(self):
        return self.name