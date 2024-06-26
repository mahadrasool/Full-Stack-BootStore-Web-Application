# Generated by Django 5.0.4 on 2024-04-17 17:05

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
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
            name='Course',
            fields=[
                ('CourseID', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('CourseName', models.CharField(max_length=255)),
                ('isArchive', models.BooleanField(default=False)),
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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('Role', models.CharField(max_length=255)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='College',
            fields=[
                ('CollegeID', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('CollegeName', models.CharField(max_length=255)),
                ('DeanID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CourseBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookstore_management.book')),
                ('Course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookstore_management.course')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='books',
            field=models.ManyToManyField(through='bookstore_management.CourseBook', to='bookstore_management.book'),
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('DepartmentCode', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('DepartmentName', models.CharField(max_length=255)),
                ('ChairID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('CollegeID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bookstore_management.college')),
            ],
        ),
        migrations.CreateModel(
            name='CourseDepartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CourseID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookstore_management.course')),
                ('DepartmentCode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookstore_management.department')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='DepartmentCode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookstore_management.department'),
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
                ('LStatus', models.CharField(choices=[('approved', 'Approved'), ('rejected', 'Rejected'), ('pending', 'Pending')], default='pending', max_length=255)),
                ('comment', models.TextField(blank=True)),
                ('CreatedByUserID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
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
                ('RequestedByUserID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('RequestedBookListID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookstore_management.requestedbooklist')),
            ],
        ),
    ]
