# tracker/admin.py

from django.contrib import admin
from .models import JobApplication

@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'job_title', 'status', 'user', 'applied_date']
    list_filter = ['status', 'applied_date']
    search_fields = ['company_name', 'job_title']