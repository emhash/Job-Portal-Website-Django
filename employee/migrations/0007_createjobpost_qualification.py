# Generated by Django 5.0.1 on 2024-01-18 14:24

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0006_companyprofile_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='createjobpost',
            name='qualification',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]