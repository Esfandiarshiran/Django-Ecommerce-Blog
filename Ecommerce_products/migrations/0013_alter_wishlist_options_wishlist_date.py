# Generated by Django 4.1 on 2022-08-10 06:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce_products', '0012_wishlist'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='wishlist',
            options={'verbose_name': 'Wish list', 'verbose_name_plural': 'Wish Lists'},
        ),
        migrations.AddField(
            model_name='wishlist',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
