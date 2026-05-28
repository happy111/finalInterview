from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import *

@admin.register(Emp)
class EmpAdmin(admin.ModelAdmin):
    pass


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass