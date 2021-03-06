# Generated by Django 3.2 on 2021-08-24 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('othernavs', '0007_auto_20210818_1507'),
    ]

    operations = [
        migrations.CreateModel(
            name='contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=50)),
                ('pincode', models.CharField(max_length=50)),
                ('time', models.DateTimeField(auto_now=True)),
                ('reg_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='othernavs.registrationsubmenu')),
            ],
        ),
    ]
