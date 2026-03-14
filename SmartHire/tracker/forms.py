# tracker/forms.py

from django import forms
from .models import JobApplication

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['company_name', 'job_title', 'location', 'salary', 'status', 'notes', 'job_url']
        widgets = {
            'company_name': forms.TextInput(attrs={'placeholder': 'e.g. Google, TCS, Infosys'}),
            'job_title': forms.TextInput(attrs={'placeholder': 'e.g. Python Developer'}),
            'location': forms.TextInput(attrs={'placeholder': 'e.g. Bangalore, Remote'}),
            'salary': forms.TextInput(attrs={'placeholder': 'e.g. 5 LPA'}),
            'notes': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Interview notes, contact person...'}),
            'job_url': forms.URLInput(attrs={'placeholder': 'https://...'}),
        }