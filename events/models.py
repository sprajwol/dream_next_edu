from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


def get_events_main_image_uploadpath(instance, filename):
    ext = filename.split('.')[-1]
    text = [
        character for character in instance.title if character.isalnum()]
    text = "".join(text)

    return f'uploads/events/{text}/{text}_image.{ext}'


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)

    def __str__(self):
        return str(self.name)

    def _get_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        num = 1
        while Category.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()

        super().save(*args, **kwargs)


class Event(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    date = models.DateField()
    main_image = models.ImageField(
        upload_to=get_events_main_image_uploadpath, blank=True, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, blank=True, null=True)
    summary = models.TextField()
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_on',)

    def __str__(self):
        return str(self.title)

    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Event.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('eventdetail', args=[str(self.slug)])
