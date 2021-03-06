# Generated by Django 3.2 on 2021-08-18 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0032_auto_20210818_1443'),
        ('othernavs', '0006_rename_optionalicon_subregistrationcontent_bannerimg'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='packageincluded',
            name='image',
        ),
        migrations.RemoveField(
            model_name='procedure',
            name='image',
        ),
        migrations.AddField(
            model_name='packageincluded',
            name='icon',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='othernavicon', to='registration.icon'),
        ),
        migrations.AddField(
            model_name='procedure',
            name='icon',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Othernavicon', to='registration.icon'),
        ),
    ]
