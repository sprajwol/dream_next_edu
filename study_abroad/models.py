from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


def get_country_main_image_uploadpath(instance, filename):
    ext = filename.split('.')[-1]
    text = [
        character for character in instance.name if character.isalnum()]
    text = "".join(text)

    return f'uploads/study_abroad/countries/{text}/{text}_image.{ext}'


class Country(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    main_image = models.ImageField(
        upload_to=get_country_main_image_uploadpath)

    def __str__(self):
        return str(self.name)

    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Country.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('single_country', args=[str(self.slug)])
