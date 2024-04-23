from django.contrib import admin
# Register your models here.
from ..models import TheUser, College, Department, Course, Publisher, Book, RequestedBookList, RequestedBook, Inventory, CourseBook, CourseDepartment
from admin_extra_buttons.api import ExtraButtonsMixin, button, confirm_action, link, view
from django.contrib.admin import AdminSite

class CollegeDean(AdminSite):
    site_header = 'College Chair'

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
    readonly_fields=['comment','LStatus', 'CreationDate', 'SchoolYear', 'DepartmentCode', 'CreatedByUserID','LName','RequestedBookListID']   

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
    list_display = ("CourseID","DepartmentCode",)
    pass

# College dean admin site models and related settings
college_admin_site = CollegeDean(name='college_admin')
college_admin_site.register(College, CollegeAdmin)
college_admin_site.register(Department, DepartmentAdmin)
college_admin_site.register(Course, CourseAdmin)
college_admin_site.register(Publisher, PublisherAdmin)
college_admin_site.register(Book, BookAdmin)
college_admin_site.register(RequestedBookList, RequestedBookListAdmin)
college_admin_site.register(RequestedBook, RequestedBookAdmin)
college_admin_site.register(Inventory, InventoryAdmin)
college_admin_site.register(CourseBook, CourseBookAdmin)
college_admin_site.register(CourseDepartment,CourseDepartmentAdmin)
