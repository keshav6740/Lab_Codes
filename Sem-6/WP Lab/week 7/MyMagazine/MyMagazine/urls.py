from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from magazine import views  # Import the views from the magazine app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('magazine/', include('magazine.urls')),  # Include the magazine app URLs
    path('', views.home, name='home'),  # Root path
]

if settings.DEBUG:

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
