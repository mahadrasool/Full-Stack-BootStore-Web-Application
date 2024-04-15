from django.contrib import admin
# Register your models here.
from .models import TheUser, College, Department, Course, Publisher, Book, RequestedBookList, RequestedBook, Inventory, CourseBook
from admin_extra_buttons.api import ExtraButtonsMixin, button, confirm_action, link, view
from django.contrib.admin import AdminSite


class DepartmentalChair(AdminSite):
    site_header = 'Departmental administration'

class CollegeDean(AdminSite):
    site_header = 'College Dean'

class CollegeAdmin(admin.ModelAdmin):
    # list_display = ('name', 'location')  # Fields to display in the list view
    # search_fields = ('name',)  # Fields to search by
    pass

class DepartmentAdmin(admin.ModelAdmin):
    # list_display = ('name', 'college')  # Fields to display in the list view
    # search_fields = ('name', 'college__name')  # Search by department name and college name
    pass

class CourseAdmin(admin.ModelAdmin):
    # list_display = ('name', 'department')  # Fields to display in the list view
    # search_fields = ('name', 'department__name')  # Search by course name and department name
    pass

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
    @button(change_form=True,
            html_attrs={'style': 'background-color:#88FF88;color:black'})
    def approve_all_books(self, request):
        # Get all book listing requests
        RequestedBookList.objects.filter().update(LStatus='approved')
        self.message_user(request, 'All Book Listing requests have been approved')
        # Optional: returns HttpResponse
        # return HttpResponseRedirectToReferrer(request)
    @button(change_form=True,
            html_attrs={'style': 'background-color:#DC6C6C;color:black'})
    def reject_all_books(self, request):
        # Get all book listing requests
        RequestedBookList.objects.filter().update(LStatus='rejected')
        self.message_user(request, 'All Book Listing requests have been rejected')
        # Optional: returns HttpResponse
        # return HttpResponseRedirectToReferrer(request)
    
class RequestedBookAdmin(admin.ModelAdmin):
    list_filter = ("DepartmentCode",)

class InventoryAdmin(admin.ModelAdmin):
    # list_display = ('book', 'quantity')  # Fields to display in the list view
    # search_fields = ('book__title',)  # Search by book title
    pass

class CourseBookAdmin(admin.ModelAdmin):
    # list_display = ('course', 'book')  # Fields to display in the list view
    # search_fields = ('course__name', 'book__title')  # Search by course name and book title
    pass


# Departmental chair admin site models and related settings
departmental_admin_site = DepartmentalChair(name='department_admin')
departmental_admin_site.register(College, CollegeAdmin)
departmental_admin_site.register(Department, DepartmentAdmin)
departmental_admin_site.register(Course, CourseAdmin)
departmental_admin_site.register(Publisher, PublisherAdmin)
departmental_admin_site.register(Book, BookAdmin)
departmental_admin_site.register(RequestedBookList, RequestedBookListAdmin)
departmental_admin_site.register(RequestedBook, RequestedBookAdmin)
departmental_admin_site.register(Inventory, InventoryAdmin)
departmental_admin_site.register(CourseBook, CourseBookAdmin)

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

admin.site.register(College)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(CourseBook)
admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(RequestedBookList)
admin.site.register(RequestedBook)
admin.site.register(Inventory)
