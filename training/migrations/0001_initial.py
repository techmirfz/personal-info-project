# Generated by Django 3.1.3 on 2020-11-11 22:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('afsn', models.CharField(blank=True, max_length=100)),
                ('coursename', models.CharField(blank=True, max_length=200)),
                ('coursedescription', models.CharField(blank=True, max_length=200)),
                ('school', models.CharField(blank=True, max_length=200)),
                ('startdate', models.CharField(blank=True, max_length=50)),
                ('enddate', models.CharField(blank=True, max_length=50)),
                ('averagegrade', models.CharField(blank=True, max_length=50)),
                ('ranking', models.CharField(blank=True, max_length=20)),
                ('numberofstudents', models.CharField(blank=True, max_length=20)),
                ('completed', models.CharField(blank=True, max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
