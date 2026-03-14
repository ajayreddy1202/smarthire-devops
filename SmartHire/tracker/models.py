# tracker/models.py

from django.db import models
from django.contrib.auth.models import User

class JobApplication(models.Model):
    
    STATUS_CHOICES = [
        ('applied', '📨 Applied'),
        ('interview', '📞 Interview Scheduled'),
        ('offer', '🎉 Offer Received'),
        ('rejected', '❌ Rejected'),
        ('withdrawn', '🔙 Withdrawn'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True)
    salary = models.CharField(max_length=50, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='applied')
    applied_date = models.DateField(auto_now_add=True)
    notes = models.TextField(blank=True)
    job_url = models.URLField(blank=True)

    def __str__(self):
        return f"{self.company_name} - {self.job_title}"

    class Meta:
        ordering = ['-applied_date']