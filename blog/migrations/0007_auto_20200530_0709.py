# Generated by Django 3.0.6 on 2020-05-30 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200530_0703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='summary',
            field=models.TextField(),
        ),
    ]