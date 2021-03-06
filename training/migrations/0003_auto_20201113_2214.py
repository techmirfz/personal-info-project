# Generated by Django 3.1.3 on 2020-11-13 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0002_auto_20201112_0705'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coursename', models.CharField(max_length=50)),
                ('coursedescription', models.CharField(max_length=50)),
                ('coursecategory', models.CharField(max_length=50)),
                ('coursefield', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='training',
            name='coursedescription',
        ),
        migrations.RemoveField(
            model_name='training',
            name='coursename',
        ),
        migrations.AddField(
            model_name='training',
            name='course',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
