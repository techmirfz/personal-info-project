# Generated by Django 3.1.6 on 2021-02-12 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_info', '0005_auto_20210212_1009'),
    ]

    operations = [
        migrations.AddField(
            model_name='basicinfo',
            name='startdate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
