# Generated by Django 3.0.8 on 2020-10-07 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tt_apis', '0028_auto_20201007_2239'),
    ]

    operations = [
        migrations.AddField(
            model_name='stucurrent',
            name='curr_level',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='stucurrent',
            name='read_level',
            field=models.IntegerField(null=True),
        ),
    ]
