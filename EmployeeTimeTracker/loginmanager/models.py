from django.db import models
from django.contrib.auth.models import User

# Create your models here.
gender_choice = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other'),
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=gender_choice, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    bank_name = models.CharField(max_length=200, null=True, blank=True)
    bank_account = models.CharField(max_length=200, null=True, blank=True)
    rate_per_hour = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.first_name