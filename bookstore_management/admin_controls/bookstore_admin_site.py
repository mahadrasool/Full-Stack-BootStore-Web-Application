from django.contrib import admin
# Register your models here.
from ..models import TheUser, College, Department, Course, Publisher, Book, RequestedBookList, RequestedBook, Inventory, CourseBook, CourseDepartment
from admin_extra_buttons.api import ExtraButtonsMixin, button, confirm_action, link, view
from django.contrib.admin import AdminSite
from django.contrib.auth.models import User, Group

class BookStoreAdministration(AdminSite):
    site_header = 'Bookstore administration'

class TheUserAdmin(ExtraButtonsMixin, admin.ModelAdmin):
    list_filter = ["Role",]

    @button(change_form=True,
            html_attrs={'style': 'background-color:#88FF88;color:black'})
    def set_all_users_staff(self, request):
        """
        This function iterates through all existing user objects and sets their is_staff field to True.
        """
        users = TheUser.objects.all()
        for user in users:
            user.is_staff = True
            user.is_superuser = True
            user.save()
        self.message_user(
            request, 'All Users have staff status set to true and they can now log into to ther respective accounts')


class CollegeAdmin(admin.ModelAdmin):
    pass


class CourseDepartmentAdmin(admin.ModelAdmin):
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
    # Search by book title and author username
    search_fields = ('BookTitle', 'Author')


class RequestedBookListAdmin(ExtraButtonsMixin, admin.ModelAdmin):
    list_filter = ("SchoolYear", "DepartmentCode",)
    # Function to handle custom button click (replace with your logic)


class RequestedBookAdmin(admin.ModelAdmin):
    list_filter = ("DepartmentCode",)


class InventoryAdmin(ExtraButtonsMixin, admin.ModelAdmin):
    @button(change_form=True,
            html_attrs={'style': 'background-color:#88FF88;color:black'})
    def send_email_to_departments(self, request):
        # Code to send email, you can add here email api code
        self.message_user(request, 'Email Sent to all departments')
        # pass

    def custom_field(self):
        # Define your custom field logic here, for example:
        department = Department.objects.get(DepartmentCode=self.DepartmentCode)
        # Assuming field1 and field2 are fields of YourModel
        return f"{self.InventoryID} - {self.BookID} - {department} - {self.CourseID} - {self.CurrentInventory} "

    # readonly_fields = ["InventoryID","BookID", "DepartmentCode","CourseID" ,"CurrentInventory"]
    list_display = [custom_field,]  # Fields to display in the list view
    list_filter = ['DepartmentCode']  # Fields to filter in the list view
    custom_field.short_description = 'Inventory ID - BookID - Department - Course Code - Current Inventory'
    search_fields = ('BookID__BookTitle',)  # Search by book title


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
bookstore_admin_site.register(CourseDepartment, CourseDepartmentAdmin)
