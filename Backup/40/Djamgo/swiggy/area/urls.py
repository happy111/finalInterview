from django.urls import path
from .views import *


urlpatterns = [
    # path("areas/", AreaCreation.as_view(), name="area-create"),                  # POST
    path("list/", ActiveAreaListing.as_view(), name="area-list"),         # GET
    # path("areas/state-city/", ActiveAreaStateCity.as_view(), name="area-state-city"),  # GET
    # path("areas/<int:pk>/update/", AreaUpdation.as_view(), name="area-update"), # PUT/PATCH
]