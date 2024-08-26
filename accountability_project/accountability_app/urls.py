from django.urls import path
from . import views


urlpatterns = [
    path("home/",views.home, name = "home"),
    path('event/<int:year>/<int:month>/<int:day>/', views.event_detail, name='event_detail'),
]