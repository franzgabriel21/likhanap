# Generated by Django 2.2.7 on 2020-02-07 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home_Business', '0004_auto_20200205_1645'),
    ]

    operations = [
        migrations.RenameField(
            model_name='portfolio',
            old_name='Profile',
            new_name='Description',
        ),
    ]
