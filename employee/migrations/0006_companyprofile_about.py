# Generated by Django 5.0.1 on 2024-01-18 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0005_createjobpost_full_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyprofile',
            name='about',
            field=models.TextField(blank=True, null=True),
        ),
    ]
