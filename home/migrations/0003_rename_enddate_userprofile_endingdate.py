# Generated by Django 4.2 on 2023-06-01 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_userprofile_city_alter_userprofile_course_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='endDate',
            new_name='endingDate',
        ),
    ]
