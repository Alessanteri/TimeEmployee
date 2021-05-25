from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class message(models.Model):
    message = models.CharField(max_length=600)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    acknowledge = models.CharField(max_length=600, null=True, blank=True)

    def __str__(self):
        return self.message