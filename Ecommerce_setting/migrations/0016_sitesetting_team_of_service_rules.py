# Generated by Django 4.0.6 on 2022-07-30 20:03

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce_setting', '0015_alter_sitesetting_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesetting',
            name='team_of_service_rules',
            field=ckeditor.fields.RichTextField(blank=True, default='Write Rules of your company in SiteManegmante', max_length=30000, null=True, verbose_name='Full descriptions'),
        ),
    ]
