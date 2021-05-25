from django.contrib import admin
from .models import DailyLog, BreakTime, MessageObject
# Register your models here.
admin.site.register(DailyLog)
admin.site.register(BreakTime)
admin.site.register(MessageObject)