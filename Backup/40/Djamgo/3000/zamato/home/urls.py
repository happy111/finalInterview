
from django.urls import path
from home.views import index, contact ,dynamic_route




urlpatterns = [
    path("",index),
    path('contact/', contact),
    path('dynamic_route/<int:number>/', dynamic_route)

]
