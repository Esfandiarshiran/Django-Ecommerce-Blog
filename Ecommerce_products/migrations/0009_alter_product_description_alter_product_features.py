# Generated by Django 4.0.6 on 2022-07-24 17:09

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce_products', '0008_alter_product_description_alter_product_features_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=ckeditor.fields.RichTextField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='product',
            name='features',
            field=ckeditor.fields.RichTextField(default='', max_length=3000, verbose_name='features'),
        ),
    ]
