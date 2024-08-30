from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name = 'accountability_app'  # This allows namespacing of URLs

urlpatterns = [
    path("home/", views.home, name="home"),
    path("public_notes/", views.public_notes, name="public_notes"),  # Added a trailing slash for consistency
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path("day_details/<int:year>/<int:month>/<int:day>/", views.day_details, name="day_details"),


    path('initiate-payment/', views.initiate_payment, name='initiate_payment'),
    path('payment-success/', views.payment_success, name='payment_success'),
    path('payment-failed/', views.payment_failed, name='payment_failed'),




    
]