# Generated by Django 4.0.6 on 2022-07-27 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce_setting', '0012_alter_sitesetting_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitesetting',
            name='facebook',
            field=models.URLField(blank=True, default='www.facebook.com', verbose_name='FaceBook Link'),
        ),
        migrations.AlterField(
            model_name='sitesetting',
            name='instagram',
            field=models.URLField(blank=True, default='www.instagram.com', verbose_name='Instagram'),
        ),
        migrations.AlterField(
            model_name='sitesetting',
            name='twitter',
            field=models.URLField(blank=True, default='www.twitter.com', verbose_name='Twitter Link'),
        ),
    ]
