from django.contrib import admin

# Register your models here.
from .models import TheUser, College, Department, Course, Publisher, Book, RequestedBookList, RequestedBook, Inventory, CourseBook

admin.site.register(TheUser)
admin.site.register(College)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(CourseBook)
admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(RequestedBookList)
admin.site.register(RequestedBook)
admin.site.register(Inventory)
