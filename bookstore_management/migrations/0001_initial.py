# Generated by Django 5.0.4 on 2024-04-12 09:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('BookID', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('BookTitle', models.CharField(max_length=255)),
                ('Author', models.CharField(max_length=255)),
                ('BookEdition', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='College',
            fields=[
                ('CollegeID', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('CollegeName', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('PublisherID', models.IntegerField(primary_key=True, serialize=False)),
                ('PublisherName', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TheUser',
            fields=[
                ('UserID', models.IntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=255)),
                ('Password', models.CharField(max_length=255)),
                ('Role', models.CharField(max_length=255)),
                ('Email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('DepartmentCode', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('DepartmentName', models.CharField(max_length=255)),
                ('CollegeID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bookstore_management.college')),
                ('ChairID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bookstore_management.theuser')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('CourseID', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('CourseName', models.CharField(max_length=255)),
                ('DepartmentCode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookstore_management.department')),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('InventoryID', models.IntegerField(primary_key=True, serialize=False)),
                ('DepartmentCode', models.CharField(max_length=4)),
                ('CourseID', models.CharField(max_length=8)),
                ('CurrentInventory', models.IntegerField()),
                ('BookID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookstore_management.book')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='PublisherID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookstore_management.publisher'),
        ),
        migrations.CreateModel(
            name='RequestedBookList',
            fields=[
                ('RequestedBookListID', models.IntegerField(primary_key=True, serialize=False)),
                ('LName', models.CharField(max_length=255)),
                ('DepartmentCode', models.CharField(max_length=4)),
                ('SchoolYear', models.CharField(max_length=10)),
                ('CreationDate', models.DateField()),
                ('LStatus', models.CharField(max_length=255)),
                ('CreatedByUserID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bookstore_management.theuser')),
            ],
        ),
        migrations.CreateModel(
            name='RequestedBook',
            fields=[
                ('RequestedBookID', models.IntegerField(primary_key=True, serialize=False)),
                ('CourseID', models.CharField(max_length=8)),
                ('DepartmentCode', models.CharField(max_length=4)),
                ('SchoolYear', models.CharField(max_length=10)),
                ('NumberedOrderForFall', models.IntegerField()),
                ('NumberedOrderForSpring', models.IntegerField()),
                ('NumberedOrderForSummer', models.IntegerField()),
                ('Approved', models.BooleanField()),
                ('BookID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookstore_management.book')),
                ('RequestedBookListID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookstore_management.requestedbooklist')),
                ('RequestedByUserID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bookstore_management.theuser')),
            ],
        ),
        migrations.AddField(
            model_name='college',
            name='DeanID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bookstore_management.theuser'),
        ),
    ]
