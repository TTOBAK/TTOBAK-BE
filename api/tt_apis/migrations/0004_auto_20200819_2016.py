# Generated by Django 3.0.8 on 2020-08-19 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tt_apis', '0003_auto_20200815_0130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stuph',
            name='ph',
        ),
        migrations.AddField(
            model_name='stuph',
            name='ph1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='ph1', to='tt_apis.PhTest'),
        ),
        migrations.AddField(
            model_name='stuph',
            name='ph2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='ph2', to='tt_apis.PhTest'),
        ),
    ]
