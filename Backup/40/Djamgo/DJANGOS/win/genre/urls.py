from django.urls import path 
from .views import *

urlpatterns = [

    path('create_genre/',GenreCreation.as_view()),
    path('update/',GenreUpdation.as_view()),
    path('delete/',GenreDeletion.as_view()),
    path("active-listing/", ActiveGenreListing.as_view()),

]


