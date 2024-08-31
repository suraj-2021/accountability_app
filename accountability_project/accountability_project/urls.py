from django.contrib import admin
from django.urls import include, path
from accountability_app import views as a

urlpatterns = [
    path ('admin/', admin.site.urls),
    
    path ('accountability_app/', include('accountability_app.urls')),  # Correctly include the app's URLs
]