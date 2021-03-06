# Generated by Django 3.2 on 2021-09-01 09:02

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0021_documents_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blognews',
            name='news',
        ),
        migrations.AddField(
            model_name='blognews',
            name='Short_des',
            field=models.CharField(default='this is short description', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blognews',
            name='content',
            field=ckeditor.fields.RichTextField(default='this is contner'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blognews',
            name='img',
            field=models.ImageField(default='s', upload_to='blogs'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blognews',
            name='last_update',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='blognews',
            name='type',
            field=models.CharField(choices=[('1', 'News'), ('2', 'Blogs')], default='1', max_length=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blognews',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
