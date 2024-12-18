# Generated by Django 3.2.7 on 2022-01-10 04:18

from django.db import migrations, models
import services.models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_rename_visa_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scholoarship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, max_length=255, null=True, unique=True)),
                ('main_image', models.ImageField(upload_to=services.models.get_scholarship_main_image_uploadpath)),
                ('summary', models.TextField()),
                ('description', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
