# Generated by Django 4.0.2 on 2022-11-14 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_rename_name_education_institute'),
    ]

    operations = [
        migrations.RenameField(
            model_name='education',
            old_name='Education',
            new_name='education',
        ),
    ]
