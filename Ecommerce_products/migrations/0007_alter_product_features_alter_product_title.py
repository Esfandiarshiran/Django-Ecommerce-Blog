# Generated by Django 4.0.6 on 2022-07-24 15:45

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce_products', '0006_product_features_alter_product_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='features',
            field=ckeditor.fields.RichTextField(default='', max_length=400, verbose_name='features'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=ckeditor.fields.RichTextField(max_length=150, verbose_name='Title'),
        ),
    ]
