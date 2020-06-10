import django_filters
from django_filters import DateFilter, CharFilter
from .models import *


class JobFilter(django_filters.FilterSet):
    job_title = CharFilter(field_name='job_title', lookup_expr='icontains')
    skills = CharFilter(field_name='skills', lookup_expr='icontains')
    job_location = CharFilter(field_name='job_location', lookup_expr='icontains')


    class Meta:
        model = Job
        fields = '__all__'
        exclude = [
            'job_description',
            'company_name',
            'Designation',
            'qualification',
            'course',
            'specialization',
            'course',
            'course_type',
            'passing_year',
            'experience',
            'salary',
            'industry',
            'job_category',
            'job_type',
            'apply'
        ]