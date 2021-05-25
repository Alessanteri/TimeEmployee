import django_filters
from django_filters import DateFilter
from .models import *


class ReportFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="checkin_time", lookup_expr='gte')
    end_date = DateFilter(field_name="checkin_time", lookup_expr='lte')

    class Meta:
        model = DailyLog
        fields = '__all__'
        exclude = ['checkin_time', 'checkout_time', 'checkin_message', 'checkout_message', 'status']