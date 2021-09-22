from django.db import models

# Create your models here.


def get_hero_slider_img_upload_path(instance, filename):
    # filename, ext = filename.split('.')
    return f'uploads/heroSlider/{filename}'


SLIDER_CONTENT_POSITION = (
    ('left', 'left'),
    ('right', 'right'),
    ('center', 'center'),
)


class HeroSlider(models.Model):
    main_text = models.CharField(max_length=255)
    sub_text = models.CharField(max_length=255)
    image = models.ImageField(
        upload_to=get_hero_slider_img_upload_path, blank=True, null=True)
    content_position = models.CharField(
        choices=SLIDER_CONTENT_POSITION, max_length=10)

    def __str__(self):
        return str(self.main_text)
