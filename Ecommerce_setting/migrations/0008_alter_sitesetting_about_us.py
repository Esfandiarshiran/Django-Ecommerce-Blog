# Generated by Django 4.0.6 on 2022-07-24 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce_setting', '0007_sitesetting_footer_logo_sitesetting_header_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitesetting',
            name='about_us',
            field=models.TextField(blank=True, max_length=400, null=True, verbose_name='Introduce company or yourself'),
        ),
    ]
