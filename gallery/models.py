from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


def get_image_upload_path(instance, filename):
    album_name = instance.photo_album
    print("album_name", album_name)

    return f'uploads/gallery/{album_name}/{filename}'


class Album(models.Model):
    photo_album_name = models.CharField(max_length=50)
    photo_album_name_slug = models.SlugField(
        max_length=255, unique=True, blank=True, null=True)
    short_desc = models.TextField()

    def __str__(self):
        return str(self.photo_album_name)

    def _get_unique_slug(self):
        slug = slugify(self.photo_album_name)
        unique_slug = slug
        num = 1
        while Album.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}_{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.photo_album_name_slug:
            self.photo_album_name_slug = self._get_unique_slug()

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('album', args=[str(self.photo_album_name_slug)])


class Image(models.Model):
    image = models.ImageField(
        upload_to=get_image_upload_path)
    photo_album = models.ForeignKey(
        Album, on_delete=models.CASCADE, default="others", related_name="images")

    def __str__(self):
        return str(self.image)
