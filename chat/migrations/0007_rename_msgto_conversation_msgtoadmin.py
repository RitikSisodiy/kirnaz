# Generated by Django 3.2 on 2021-08-15 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0006_alter_conversation_msgto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='conversation',
            old_name='msgto',
            new_name='msgtoadmin',
        ),
    ]
