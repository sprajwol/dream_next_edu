# Generated by Django 3.2.7 on 2021-11-02 01:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='heroslider',
            name='content_position',
        ),
    ]
