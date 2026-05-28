from django.urls import path
from .views import *
urlpatterns = [
    path("create/", AreaCreation.as_view()),
    path("area-listing/", ActiveAreaListing.as_view()),
    path("area_state_city/", ActiveAreaStateCity.as_view()),
    path("area_update/", AreaUpdation.as_view()),
]
