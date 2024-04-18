from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.core.exceptions import ObjectDoesNotExist

class TheUser(AbstractUser):
    Role = models.CharField(max_length=255)
    id = models.IntegerField(primary_key=True)
    
    def __str__(self) -> str:
        return f"{self.id} , {self.username}"
    
class College(models.Model):
    CollegeID = models.CharField(max_length=20, primary_key=True)
    CollegeName = models.CharField(max_length=255)
    DeanID = models.ForeignKey(TheUser, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.CollegeName


class Department(models.Model):
    DepartmentCode = models.CharField(max_length=4, primary_key=True)
    DepartmentName = models.CharField(max_length=255)
    CollegeID = models.ForeignKey(
        College, on_delete=models.SET_NULL, null=True)
    ChairID = models.ForeignKey(TheUser, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.DepartmentName


class Course(models.Model):
    CourseID = models.CharField(max_length=8, primary_key=True)
    CourseName = models.CharField(max_length=255)
    DepartmentCode = models.ForeignKey(Department, on_delete=models.CASCADE)
    # Linking Course with Book
    books = models.ManyToManyField('Book', through='CourseBook')
    isArchive = models.BooleanField(default=False)

    def __str__(self):
        return self.CourseName


class Publisher(models.Model):
    PublisherID = models.IntegerField(primary_key=True)
    PublisherName = models.CharField(max_length=255)

    def __str__(self):
        return self.PublisherName


class Book(models.Model):
    BookID = models.CharField(max_length=255, primary_key=True)
    BookTitle = models.CharField(max_length=255)
    Author = models.CharField(max_length=255)
    BookEdition = models.CharField(max_length=50)
    PublisherID = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    def __str__(self):
        return self.BookTitle


class CourseBook(models.Model):
    Course = models.ForeignKey(Course, on_delete=models.CASCADE)
    Book = models.ForeignKey(Book, on_delete=models.CASCADE)

class CourseDepartment(models.Model):
    CourseID = models.ForeignKey(Course, on_delete=models.CASCADE)
    DepartmentCode = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return f"Course: {self.CourseID} | Department: {self.DepartmentCode}"
            

class RequestedBookList(models.Model):
    RequestedBookListID = models.IntegerField(primary_key=True)
    LName = models.CharField(max_length=255)
    CreatedByUserID = models.ForeignKey(
        TheUser, on_delete=models.SET_NULL, null=True)
    DepartmentCode = models.CharField(max_length=4)
    SchoolYear = models.CharField(max_length=10)
    CreationDate = models.DateField()
    LSTATUS_CHOICES = (
    ('approved', 'Approved'),
    ('rejected', 'Rejected'),
    ('pending', 'Pending'),
    )
    LStatus = models.CharField(max_length=255, choices=LSTATUS_CHOICES, default='pending')  # Set default to 'approved'
    comment = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.LName} requested by {self.DepartmentCode}"
     
class RequestedBook(models.Model):
    RequestedBookID = models.IntegerField(primary_key=True)
    BookID = models.ForeignKey(Book, on_delete=models.CASCADE)
    RequestedBookListID = models.ForeignKey(
        RequestedBookList, on_delete=models.CASCADE)
    CourseID = models.CharField(max_length=8)
    DepartmentCode = models.CharField(max_length=4)
    SchoolYear = models.CharField(max_length=10)
    RequestedByUserID = models.ForeignKey(
        TheUser, on_delete=models.SET_NULL, null=True)
    NumberedOrderForFall = models.IntegerField()
    NumberedOrderForSpring = models.IntegerField()
    NumberedOrderForSummer = models.IntegerField()
    Approved = models.BooleanField()
    
    def __str__(self):
        return f"{self.RequestedBookID}: {self.BookID}"

class Inventory(models.Model):
    InventoryID = models.IntegerField(primary_key=True)
    BookID = models.ForeignKey(Book, on_delete=models.CASCADE)
    DepartmentCode = models.CharField(max_length=4)
    CourseID = models.CharField(max_length=8)
    CurrentInventory = models.IntegerField()

    def __str__(self):
        return f"Inventory ID: {self.InventoryID}, Book: {self.BookID.BookTitle}, Department: {self.DepartmentCode}, Course: {self.CourseID}"
