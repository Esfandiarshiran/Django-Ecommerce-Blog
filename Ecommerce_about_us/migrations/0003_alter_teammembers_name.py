# Generated by Django 4.0.6 on 2022-07-24 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce_about_us', '0002_alter_teammembers_email_alter_teammembers_introduce_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammembers',
            name='name',
            field=models.CharField(max_length=150, verbose_name='Name'),
        ),
    ]