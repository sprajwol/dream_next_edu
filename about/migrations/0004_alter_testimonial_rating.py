# Generated by Django 3.2.7 on 2021-10-30 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_testimonial_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='rating',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=10),
        ),
    ]
