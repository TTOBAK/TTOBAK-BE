# Generated by Django 3.0.8 on 2020-08-25 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tt_apis', '0009_auto_20200825_0101'),
    ]

    operations = [
        migrations.CreateModel(
            name='FocScript',
            fields=[
                ('fs_id', models.AutoField(primary_key=True, serialize=False)),
                ('conv_id', models.IntegerField()),
                ('script', models.CharField(max_length=1000)),
            ],
        ),
    ]
