# Generated by Django 4.1 on 2022-08-12 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce_User_Dashboard', '0006_alter_userprofile_birth_day'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(default='', max_length=150, verbose_name='email'),
        ),
    ]
