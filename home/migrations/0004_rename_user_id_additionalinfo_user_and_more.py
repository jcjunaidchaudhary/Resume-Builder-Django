# Generated by Django 4.0.2 on 2022-11-12 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_rename_objctive_personal_objective_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='additionalinfo',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='personal',
            old_name='user_id',
            new_name='user',
        ),
    ]
