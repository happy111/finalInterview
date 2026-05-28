from django.db import models
from common.models import Common

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


class State(Common):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="State Name")

    area = models.ForeignKey(
        Area,
        related_name='State_state',
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Area',
        limit_choices_to={'active_status': '1'})



    class Meta:
        verbose_name = "State"
        verbose_name_plural = "State"

    def __str__(self):
        return self.name


class City(Common):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="City Name")

    state = models.ForeignKey(
        State,
        related_name='City_city',
        on_delete=models.CASCADE,
        null=True,
        verbose_name='State',
        limit_choices_to={'active_status': '1'})


    class Meta:
        verbose_name = "City"
        verbose_name_plural = "City"

    def __str__(self):
        return self.name