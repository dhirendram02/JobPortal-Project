# Generated by Django 4.1.5 on 2023-03-03 06:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobseeker', '0005_rename_career1_career'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Career',
            new_name='Jobapp',
        ),
    ]