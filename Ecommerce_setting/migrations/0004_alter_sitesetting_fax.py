# Generated by Django 4.0.6 on 2022-07-22 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce_setting', '0003_alter_sitesetting_options_alter_sitesetting_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitesetting',
            name='fax',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Fax'),
        ),
    ]