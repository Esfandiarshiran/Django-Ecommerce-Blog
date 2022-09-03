# Generated by Django 4.0.6 on 2022-07-24 20:59

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce_setting', '0010_rename_introduce_sitesetting_introduce'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesetting',
            name='description',
            field=ckeditor.fields.RichTextField(default='', max_length=30000, verbose_name='Full descriptions'),
        ),
        migrations.AlterField(
            model_name='sitesetting',
            name='introduce',
            field=models.TextField(blank=True, max_length=400, null=True, verbose_name='Who you are ?'),
        ),
    ]