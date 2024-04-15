from django.urls import path, include
from .admin_controls import college_admin_site, department_admin_site, bookstore_admin_site

urlpatterns = [
    path('department/', department_admin_site.departmental_admin_site.urls),
    path('college/', college_admin_site.college_admin_site.urls),
    path('bookstore/',bookstore_admin_site.bookstore_admin_site.urls)
    # ... other URL patterns
]