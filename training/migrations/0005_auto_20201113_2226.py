# Generated by Django 3.1.3 on 2020-11-13 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0004_auto_20201113_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='training',
            name='course',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
