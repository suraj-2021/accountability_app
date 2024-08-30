from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path ('admin/', admin.site.urls),

    path ('accountability_app/', include('accountability_app.urls')),  # Correctly include the app's URLs
]