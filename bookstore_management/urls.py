from django.urls import path, include
from .admin import departmental_admin_site, college_admin_site

urlpatterns = [
    path('department/', departmental_admin_site.urls),
    path('college/', college_admin_site.urls),
    # ... other URL patterns
]