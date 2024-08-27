from django.urls import path
from . import views


urlpatterns = [
    path("home/",views.home, name = "home"),
    path("day_details/<int:year>/<int:month>/<int:day>",views.day_details, name = "day_details"),
   
]