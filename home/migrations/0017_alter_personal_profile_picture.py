# Generated by Django 4.0.2 on 2022-11-17 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_alter_personal_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal',
            name='profile_picture',
            field=models.ImageField(upload_to='profile picture'),
        ),
    ]
