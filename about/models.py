from django.db import models

from home.image_compress import compressImage
# Create your models here.


def get_reviewer_image_uploadpath(instance, filename):
    ext = filename.split('.')[-1]
    full_name = [
        character for character in instance.reviewer if character.isalnum()]
    full_name = "".join(full_name)

    return f'uploads/about/testimonials/{full_name}/{full_name}_image.{ext}'


def get_member_image_uploadpath(instance, filename):
    ext = filename.split('.')[-1]
    full_name = [
        character for character in instance.reviewer if character.isalnum()]
    full_name = "".join(full_name)

    return f'uploads/about/members/{full_name}/{full_name}_image.{ext}'


class Testimonial(models.Model):
    reviewer = models.CharField(
        max_length=100, verbose_name='Reviewer Full Name')
    designation = models.CharField(
        max_length=50, verbose_name='Reviewer Designation')
    image = models.ImageField(upload_to=get_reviewer_image_uploadpath,
                              blank=True, null=True, verbose_name='Reviewer Image')
    testimony = models.TextField()
    created_at = models.DateField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateField(auto_now=True, verbose_name='Updated at')

    __original_image = None

    def __str__(self):
        return str(self.reviewer)

    def __init__(self, *args, **kwargs):
        super(Testimonial, self).__init__(*args, **kwargs)
        if self.image:
            self.__original_image = self.image

    def save(self, *args, **kwargs):
        # print("in save")
        # print("in save", self.image)
        if self.image:
            if self.image != self.__original_image:
                self.image = compressImage(self.image)

        super(Testimonial, self).save(*args, **kwargs)


class Member(models.Model):
    full_name = models.CharField(
        max_length=100, verbose_name='Member Full Name')
    image = models.ImageField(upload_to=get_member_image_uploadpath,
                              blank=True, null=True, verbose_name='Member Image')
    position = models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateField(auto_now=True, verbose_name='Updated at')

    __original_image = None

    def __str__(self):
        return str(self.full_name)

    def __init__(self, *args, **kwargs):
        super(Member, self).__init__(*args, **kwargs)
        if self.image:
            self.__original_image = self.image

    def save(self, *args, **kwargs):
        # print("in save")
        # print("in save", self.image)
        if self.image:
            if self.image != self.__original_image:
                self.image = compressImage(self.image)

        super(Member, self).save(*args, **kwargs)
