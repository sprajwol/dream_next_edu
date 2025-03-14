# Generated by Django 3.2.7 on 2021-10-25 08:58

import about.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, verbose_name='Member Full Name')),
                ('image', models.ImageField(blank=True, null=True, upload_to=about.models.get_member_image_uploadpath, verbose_name='Member Image')),
                ('position', models.CharField(max_length=50)),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Updated at')),
            ],
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=about.models.get_reviewer_image_uploadpath, verbose_name='Reviewer Image'),
        ),
    ]
