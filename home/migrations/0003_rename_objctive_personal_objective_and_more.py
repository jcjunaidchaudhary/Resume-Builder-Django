# Generated by Django 4.0.2 on 2022-11-12 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_profile_image_personal_profile_picture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personal',
            old_name='objctive',
            new_name='objective',
        ),
        migrations.RenameField(
            model_name='personal',
            old_name='user',
            new_name='user_id',
        ),
    ]