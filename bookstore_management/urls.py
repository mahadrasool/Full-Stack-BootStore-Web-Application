from django.urls import path, include
from .admin_controls import college_admin_site, department_admin_site, bookstore_admin_site
from .views import inventory_report, generate_report, home

urlpatterns = [
    path('', home, name='home'),
    path('department/', department_admin_site.departmental_admin_site.urls),
    path('college/', college_admin_site.college_admin_site.urls),
    path('bookstore/',bookstore_admin_site.bookstore_admin_site.urls),
    path('inventory_report/', inventory_report, name='inventory_report'),
    path('generate_report/', generate_report, name='generate_report'),
]