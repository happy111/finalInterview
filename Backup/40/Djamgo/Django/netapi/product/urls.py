from django.urls import path
from .views import *

urlpatterns = [
    path("create/", CategoryCreation.as_view()),
    path("list/", CategoryListing.as_view()),


    # path("delete/", AreaDeletion.as_view()),
   #  path("active-listing/", ActiveAreaListing.as_view()),
    # path("all-listing/", AllAreaListing.as_view()),
    # path("update/", AreaUpdation.as_view()),
  #  path("area_state_city/", ActiveAreaStateCity.as_view()),
]
