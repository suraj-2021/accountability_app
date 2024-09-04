from django.contrib import admin
from django.urls import include, path
from accountability_app import views as a

urlpatterns = [
    path ('admin/', admin.site.urls),    
    #path ('', include('accountability_app.urls')),
    path('accountability_app/',include('accountability_app.urls')),
    path(' ', include('pwa.urls')),
        ]