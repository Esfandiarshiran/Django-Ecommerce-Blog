# Generated by Django 4.0.6 on 2022-07-23 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce_Contact', '0004_alter_contactus_is_read'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='is_read',
            field=models.BooleanField(default=False, verbose_name='Read'),
        ),
    ]
