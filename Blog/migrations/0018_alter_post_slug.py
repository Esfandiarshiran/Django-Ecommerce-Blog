# Generated by Django 4.1 on 2022-08-07 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0017_post_visit_count_alter_post_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.CharField(max_length=300, unique=True),
        ),
    ]
