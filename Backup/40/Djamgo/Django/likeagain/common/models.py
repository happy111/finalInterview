from django.db import models

# Create your models here.

class Common(models.Model):
	active_status = models.BooleanField(
		default=True, 
		null=True, 
		blank=True)
	created_at = models.DateTimeField(
		auto_now_add=True,
		null=True,
		blank=True, 
		editable=False)
	updated_at = models.DateTimeField(
		auto_now=True,
		null=True,
		blank=True)

	class Meta:
		abstract=True