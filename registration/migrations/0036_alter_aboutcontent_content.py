# Generated by Django 3.2 on 2021-08-27 12:36

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0035_aboutcontent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutcontent',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, max_length=5000, null=True),
        ),
    ]