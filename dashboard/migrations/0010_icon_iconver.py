# Generated by Django 3.2 on 2021-08-17 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_auto_20210815_1732'),
    ]

    operations = [
        migrations.CreateModel(
            name='iconver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='icon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=70)),
                ('version', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.iconver')),
            ],
        ),
    ]
