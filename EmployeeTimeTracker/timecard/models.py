from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class MessageObject(models.Model):
    message_object = models.CharField(max_length=600)
    date_created_object = models.DateTimeField(auto_now_add=True, null=True)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    #acknowledge = models.CharField(max_length=600, null=True, blank=True)

    def __str__(self):
        return self.message_object


# Create your models here.
class DailyLog(models.Model):
    checkin_time = models.DateTimeField(default=datetime.now, null=True, blank=True)
    checkout_time = models.DateTimeField(default=datetime.now, blank=True)
    message_object = models.CharField(max_length=500, null=True, blank=True)
    status = models.IntegerField(blank=True, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str('%s %s %s' % (self.checkin_time, self.user, self.message_object))


class BreakTime(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    time_period = models.TimeField(blank=False, null=False)

    def __str__(self):
        return str('%s %s' % (self.time_period, self.name))


class ObjectName(models.Model):
    object_name = models.CharField(default="default object", max_length=600)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    acknowledge = models.CharField(max_length=600, null=True, blank=True)

    def __str__(self):
        return self.object_name




