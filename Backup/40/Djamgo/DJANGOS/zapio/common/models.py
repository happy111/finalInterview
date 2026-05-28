from django.db import models


class Common(models.Model):
    active_status = models.BooleanField(
        default=1,
        null=True,
        blank=True,
        verbose_name="Area Active Status"
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
        abstract = True

