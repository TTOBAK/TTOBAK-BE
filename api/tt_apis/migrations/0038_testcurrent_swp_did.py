# Generated by Django 3.0.8 on 2020-10-12 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tt_apis', '0037_stutest_is_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='testcurrent',
            name='swp_did',
            field=models.IntegerField(null=True),
        ),
    ]
