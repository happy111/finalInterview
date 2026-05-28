
from django.urls import path
from .views import *


urlpatterns = [
   path("create/",AreaCreation.as_view(), name="area-create")


]