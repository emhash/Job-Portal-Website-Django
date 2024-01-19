# Generated by Django 5.0.1 on 2024-01-19 15:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0010_company_remove_companyprofile_about_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='first_employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.employeeprofile'),
        ),
    ]