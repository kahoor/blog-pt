# Generated by Django 3.0.6 on 2020-05-29 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200528_0253'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='read_time',
            field=models.IntegerField(default=0),
        ),
    ]
