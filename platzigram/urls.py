"""
    Platizagram URLs module.
"""

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Posts
    path('', include('posts.urls')),

    # Users
    path('users/', include('users.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
