# Generated by Django 3.2 on 2021-08-14 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('othernavs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subregistrationcontent',
            old_name='submenu',
            new_name='reg_title',
        ),
    ]
