from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


def get_visa_services_main_image_uploadpath(instance, filename):
    ext = filename.split('.')[-1]
    text = [
        character for character in instance.title if character.isalnum()]
    text = "".join(text)

    return f'uploads/services/visa/{text}/{text}_image.{ext}'

def get_scholarship_main_image_uploadpath(instance, filename):
    ext = filename.split('.')[-1]
    text = [
        character for character in instance.title if character.isalnum()]
    text = "".join(text)

    return f'uploads/services/scholarship/{text}/{text}_image.{ext}'


class Service(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    main_image = models.ImageField(
        upload_to=get_visa_services_main_image_uploadpath)
    summary = models.TextField()
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)

    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Service.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('services_detail', args=[str(self.slug)])


class Scholoarship(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    main_image = models.ImageField(
        upload_to=get_scholarship_main_image_uploadpath)
    summary = models.TextField()
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)

    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Scholoarship.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('scholarships_detail', args=[str(self.slug)])