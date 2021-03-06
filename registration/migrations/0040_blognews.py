# Generated by Django 3.2.6 on 2022-01-31 17:16

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0039_registration_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('type', models.CharField(choices=[('1', 'News'), ('2', 'Blogs'), ('3', 'Article')], max_length=1)),
                ('img', models.ImageField(upload_to='blogs')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('Short_des', models.CharField(max_length=500)),
                ('content', ckeditor.fields.RichTextField()),
                ('reg_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.registrationsubmenu')),
            ],
        ),
    ]
