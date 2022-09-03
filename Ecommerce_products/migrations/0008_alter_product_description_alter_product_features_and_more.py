# Generated by Django 4.0.6 on 2022-07-24 16:16

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce_products', '0007_alter_product_features_alter_product_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=ckeditor.fields.RichTextField(max_length=3000),
        ),
        migrations.AlterField(
            model_name='product',
            name='features',
            field=ckeditor.fields.RichTextField(default='', max_length=500, verbose_name='features'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=150, verbose_name='Title'),
        ),
    ]