# Generated by Django 3.2 on 2021-08-17 06:40

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0011_aboutca'),
    ]

    operations = [
        migrations.CreateModel(
            name='addblog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='blogsimg')),
                ('conntent', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
        ),
    ]
