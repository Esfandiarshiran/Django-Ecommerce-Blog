# Generated by Django 4.0.6 on 2022-08-03 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0004_alter_post_options_rename_create_date_post_create_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-publish_date',)},
        ),
        migrations.RenameField(
            model_name='post',
            old_name='create',
            new_name='create_date',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='publish',
            new_name='publish_date',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='update',
            new_name='update_date',
        ),
    ]