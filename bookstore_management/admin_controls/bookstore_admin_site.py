from django.contrib import admin
# Register your models here.
from ..models import TheUser, College, Department, Course, Publisher, Book, RequestedBookList, RequestedBook, Inventory, CourseBook
from admin_extra_buttons.api import ExtraButtonsMixin, button, confirm_action, link, view
from django.contrib.admin import AdminSite

class BookStoreAdministration(AdminSite):
    site_header = 'Principal administration'

class TheUserAdmin(admin.ModelAdmin):
    pass

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
    # Function to handle custom button click (replace with your logic)
    
class RequestedBookAdmin(admin.ModelAdmin):
    list_filter = ("DepartmentCode",)

class InventoryAdmin(admin.ModelAdmin):
    list_display = ('DepartmentCode',)  # Fields to display in the list view
    # search_fields = ('book__title',)  # Search by book title
    pass

class CourseBookAdmin(admin.ModelAdmin):
    list_display = ('Book', 'Course')  # Fields to display in the list view
    search_fields = ('Course', 'Book')  # Search by course name and book title

    def get_queryset(self, request):
        # Filter courses to show only active ones (isArchive=False)
        queryset = super().get_queryset(request)
        return queryset.filter(Course__isArchive=False)

bookstore_admin_site = BookStoreAdministration()
bookstore_admin_site.register(TheUser, TheUserAdmin)
bookstore_admin_site.register(College, CollegeAdmin)
bookstore_admin_site.register(Department, DepartmentAdmin)
bookstore_admin_site.register(Course, CourseAdmin)
bookstore_admin_site.register(Publisher, PublisherAdmin)
bookstore_admin_site.register(Book, BookAdmin)
bookstore_admin_site.register(RequestedBookList, RequestedBookListAdmin)
bookstore_admin_site.register(RequestedBook, RequestedBookAdmin)
bookstore_admin_site.register(Inventory, InventoryAdmin)
bookstore_admin_site.register(CourseBook, CourseBookAdmin)
