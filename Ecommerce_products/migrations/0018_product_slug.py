# Generated by Django 4.1 on 2022-08-17 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce_products', '0017_alter_product_discount_alter_product_zip_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, max_length=400),
        ),
    ]
