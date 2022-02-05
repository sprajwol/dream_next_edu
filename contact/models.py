from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

ABOUT_CHOICES = (
    ("visa-application", "Visa Application"),
    ("test-preparation", "Test Preparation"),
    ("consultation", "Consultation"),
)

MARITAL_STATUS_CHOICES = (
    ("married", "Married"),
    ("unmarried", "Unmarried")
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

class Enquiry(models.Model):
    full_name = models.CharField(
        max_length=100, verbose_name='Full Name')
    dob = models.CharField(max_length=50)
    passport_number = models.CharField(max_length=50)
    qualification = models.CharField(max_length=50)
    college_name = models.CharField(max_length=50)
    grade_or_percent = models.CharField(max_length=10)
    passed_year = models.CharField(max_length=10, verbose_name='Passed Year')
    marital_status = models.CharField(choices=MARITAL_STATUS_CHOICES, max_length=20, verbose_name='Marital Status')
    address = models.CharField(max_length=50, verbose_name='Address')
    mobile_number_regex = RegexValidator(
        regex=r'^[0-9]*$', message="Only numbers is allowed")
    contact = models.CharField(max_length=20, validators=[mobile_number_regex])
    email = models.EmailField(max_length=100, verbose_name='Email Address')
    guardian_contact = models.CharField(max_length=20, validators=[mobile_number_regex])
    country_to_apply = models.CharField(max_length=50)
    desired_course = models.CharField(max_length=50)
    taken_educational_institution = models.BooleanField()
    chosen_educational_institution = models.CharField(max_length=255)
    how_know_about_use = models.TextField()

    def __str__(self):
        return str(self.full_name)