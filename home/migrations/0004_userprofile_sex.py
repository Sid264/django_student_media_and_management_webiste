# Generated by Django 4.2 on 2023-06-01 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_rename_enddate_userprofile_endingdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='sex',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
