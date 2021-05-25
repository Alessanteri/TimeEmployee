from django.db import models

# Create your models here.
class test(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True, blank=True)
    email = models.EmailField(max_length=200)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name