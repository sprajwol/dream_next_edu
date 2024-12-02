from django.db import models

from home.image_compress import compressImage

# Create your models here.


def get_hero_slider_img_upload_path(instance, filename):
    # filename, ext = filename.split('.')
    return f'uploads/heroSlider/{filename}'


class HeroSlider(models.Model):
    main_text = models.CharField(max_length=255)
    sub_text = models.CharField(max_length=255)
    image = models.ImageField(
        upload_to=get_hero_slider_img_upload_path, blank=True, null=True)

    __original_image = None

    def __str__(self):
        return str(self.main_text)

    def __init__(self, *args, **kwargs):
        super(HeroSlider, self).__init__(*args, **kwargs)
        if self.image:
            self.__original_image = self.image

    def save(self, *args, **kwargs):
        # print("in save")
        # print("in save", self.image)
        if self.image:
            if self.image != self.__original_image:
                self.image = compressImage(self.image)

        super(HeroSlider, self).save(*args, **kwargs)
