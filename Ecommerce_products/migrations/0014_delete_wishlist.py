# Generated by Django 4.1 on 2022-08-10 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce_products', '0013_alter_wishlist_options_wishlist_date'),
    ]

    operations = [
        migrations.DeleteModel(
            name='WishList',
        ),
    ]
