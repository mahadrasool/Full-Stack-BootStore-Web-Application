from django.contrib import admin
# Register your models here.
from ..models import TheUser, College, Department, Course, Publisher, Book, RequestedBookList, RequestedBook, Inventory, CourseBook, CourseDepartment
from admin_extra_buttons.api import ExtraButtonsMixin, button, confirm_action, link, view
from django.contrib.admin import AdminSite

class DepartmentalChair(AdminSite):
    site_header = 'Departmental Dean'

class CollegeAdmin(admin.ModelAdmin):
    # list_display = ('name', 'location')  # Fields to display in the list view
    # search_fields = ('name',)  # Fields to search by
    pass

class DepartmentAdmin(admin.ModelAdmin):
    # list_display = ('name', 'college')  # Fields to display in the list view
    # search_fields = ('name', 'college__name')  # Search by department name and college name
    pass

class CourseAdmin(admin.ModelAdmin):
    # list_display = ('isArchive',)  # Fields to display in the list view
    # search_fields = ('name', 'department__name')  # Search by course name and department name
    list_filter = ('isArchive',) 
    
class PublisherAdmin(admin.ModelAdmin):
    # list_display = ('name', 'location')  # Fields to display in the list view
    # search_fields = ('name',)  # Search by publisher name
    pass

class BookAdmin(admin.ModelAdmin):
    # list_display = ('title', 'authors', 'publisher')  # Fields to display in the list view
    search_fields = ('BookTitle', 'Author')  # Search by book title and author username

class RequestedBookListAdmin(ExtraButtonsMixin, admin.ModelAdmin):
    list_filter = ("SchoolYear","DepartmentCode",)
    readonly_fields =("LStatus",)

class RequestedBookAdmin(admin.ModelAdmin):
    list_filter = ("DepartmentCode",)

class InventoryAdmin(admin.ModelAdmin):
    # list_display = ('book', 'quantity')  # Fields to display in the list view
    # search_fields = ('book__title',)  # Search by book title
    pass

class CourseBookAdmin(admin.ModelAdmin):
    list_display = ('Book', 'Course')  # Fields to display in the list view
    search_fields = ('Course', 'Book')  # Search by course name and book title

    def get_queryset(self, request):
        # Filter courses to show only active ones (isArchive=False)
        queryset = super().get_queryset(request)
        return queryset.filter(Course__isArchive=False)

class CourseDepartmentAdmin(admin.ModelAdmin):
    pass

# Departmental chair admin site models and related settings
departmental_admin_site = DepartmentalChair(name='department_admin')
departmental_admin_site.register(College, CollegeAdmin)
departmental_admin_site.register(Department, DepartmentAdmin)
departmental_admin_site.register(Course, CourseAdmin)
departmental_admin_site.register(Publisher, PublisherAdmin)
departmental_admin_site.register(Book, BookAdmin)
departmental_admin_site.register(RequestedBookList, RequestedBookListAdmin)
# departmental_admin_site.register(RequestedBook, RequestedBookAdmin)
departmental_admin_site.register(Inventory, InventoryAdmin)
departmental_admin_site.register(CourseBook, CourseBookAdmin)
departmental_admin_site.register(CourseDepartment,CourseDepartmentAdmin)

