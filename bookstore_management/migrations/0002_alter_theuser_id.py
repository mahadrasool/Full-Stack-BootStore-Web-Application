# Generated by Django 5.0.4 on 2024-04-18 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theuser',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]