# Generated by Django 4.0.2 on 2022-11-14 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_rename_social_profile_socialprofile_social_profile_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additionalinfo',
            name='Language',
            field=models.CharField(max_length=150),
        ),
    ]