from django.contrib import admin

# Register your models here.
from .models import Area

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    pass