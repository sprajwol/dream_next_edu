from django.db import models

# Create your models here.

ABOUT_CHOICES = (
    ("visa-application", "Visa Application"),
    ("test-preparation", "Test Preparation"),
    ("consultation", "Consultation"),
)


class Contact(models.Model):
    full_name = models.CharField(
        max_length=100, verbose_name='Full Name')
    email = models.EmailField(max_length=100, verbose_name='Email Address')
    contact = models.CharField(
        max_length=20, blank=True, null=True, verbose_name='Contact Number')
    about = models.CharField(choices=ABOUT_CHOICES,
                             max_length=20, blank=True, null=True, verbose_name='Enquiry About')
    message = models.TextField(verbose_name='Message')

    def __str__(self):
        return str(self.full_name)
