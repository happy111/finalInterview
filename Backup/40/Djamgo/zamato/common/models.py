from django.db import models

# Create your models here.

class Common(models.Model):
    active_statis = models.BooleanField(
        default=True,
        null=True,
        blank=True,

    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True,
        editable=False,
        verbose_name="Creation Date & Time"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        null=True,
        blank=True,
        verbose_name="Update Date & Time"
    )

    class Meta:
        abstract = True
