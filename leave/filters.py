import django_filters

from .models import *

class LeaveFilter(django_filters.FilterSet):
    class Meta:
        model = apply
        fields = '__all__'
        exclude = ['employee','from_date','to_date','from_time','to_time','reason','date_created','status1','date']

