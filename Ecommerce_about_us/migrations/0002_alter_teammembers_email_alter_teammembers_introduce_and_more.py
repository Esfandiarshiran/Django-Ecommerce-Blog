# Generated by Django 4.0.6 on 2022-07-24 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce_about_us', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammembers',
            name='email',
            field=models.CharField(max_length=150, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='teammembers',
            name='introduce',
            field=models.CharField(max_length=300, verbose_name='Introduce'),
        ),
        migrations.AlterField(
            model_name='teammembers',
            name='job_title',
            field=models.CharField(max_length=150, verbose_name='Job Title'),
        ),
    ]
