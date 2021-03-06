# Generated by Django 3.2.7 on 2021-09-22 16:13

from django.db import migrations, models
import home.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HeroSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_text', models.CharField(max_length=255)),
                ('sub_text', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to=home.models.get_hero_slider_img_upload_path)),
                ('content_position', models.CharField(choices=[('left', 'left'), ('right', 'right'), ('center', 'center')], max_length=10)),
            ],
        ),
    ]
