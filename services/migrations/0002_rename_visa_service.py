# Generated by Django 3.2.7 on 2021-11-03 04:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Visa',
            new_name='Service',
        ),
    ]