# Generated by Django 4.0.6 on 2022-07-24 21:10

import Ecommerce_about_us.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TeamMembers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Title')),
                ('job_title', models.CharField(max_length=150, verbose_name='Title')),
                ('introduce', models.CharField(max_length=300, verbose_name='Title')),
                ('picture', models.ImageField(upload_to=Ecommerce_about_us.models.upload_image_path, verbose_name='Picture')),
                ('email', models.CharField(max_length=150, verbose_name='Title')),
            ],
        ),
    ]
