# Generated by Django 3.2 on 2021-08-14 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0026_ourclients_name'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='registrationsubmenu',
            unique_together={('title', 'submenu')},
        ),
    ]
