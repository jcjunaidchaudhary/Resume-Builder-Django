# Generated by Django 4.0.2 on 2022-11-17 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_alter_personal_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal',
            name='profile_picture',
            field=models.ImageField(default='', upload_to='profile picture'),
        ),
    ]