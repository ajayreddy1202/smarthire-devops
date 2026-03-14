# tracker/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count
from .models import JobApplication
from .forms import JobApplicationForm

# ─── REGISTER ───────────────────────────────────
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created! Welcome to SmartHire 🎉")
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'tracker/register.html', {'form': form})

# ─── LOGIN ───────────────────────────────────────
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid credentials!")
    else:
        form = AuthenticationForm()
    return render(request, 'tracker/login.html', {'form': form})

# ─── LOGOUT ──────────────────────────────────────
def logout_view(request):
    logout(request)
    return redirect('login')

# ─── DASHBOARD ───────────────────────────────────
@login_required
def dashboard(request):
    jobs = JobApplication.objects.filter(user=request.user)
    
    # Stats for cards
    total = jobs.count()
    interviews = jobs.filter(status='interview').count()
    offers = jobs.filter(status='offer').count()
    rejected = jobs.filter(status='rejected').count()

    # Data for pie chart (JavaScript will use this)
    status_data = jobs.values('status').annotate(count=Count('status'))
    chart_labels = [item['status'] for item in status_data]
    chart_values = [item['count'] for item in status_data]

    context = {
        'jobs': jobs[:5],  # Recent 5
        'total': total,
        'interviews': interviews,
        'offers': offers,
        'rejected': rejected,
        'chart_labels': chart_labels,
        'chart_values': chart_values,
    }
    return render(request, 'tracker/dashboard.html', context)

# ─── ALL JOBS LIST ────────────────────────────────
@login_required
def job_list(request):
    jobs = JobApplication.objects.filter(user=request.user)
    
    # Search filter
    search = request.GET.get('search', '')
    status_filter = request.GET.get('status', '')
    
    if search:
        jobs = jobs.filter(company_name__icontains=search)
    if status_filter:
        jobs = jobs.filter(status=status_filter)
    
    return render(request, 'tracker/job_list.html', {
        'jobs': jobs,
        'search': search,
        'status_filter': status_filter,
    })

# ─── ADD JOB ─────────────────────────────────────
@login_required
def add_job(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.user = request.user
            job.save()
            messages.success(request, "Job added successfully! 🚀")
            return redirect('job_list')
    else:
        form = JobApplicationForm()
    return render(request, 'tracker/add_job.html', {'form': form})

# ─── EDIT JOB ────────────────────────────────────
@login_required
def edit_job(request, pk):
    job = get_object_or_404(JobApplication, pk=pk, user=request.user)
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            messages.success(request, "Job updated!")
            return redirect('job_list')
    else:
        form = JobApplicationForm(instance=job)
    return render(request, 'tracker/add_job.html', {'form': form, 'edit': True})

# ─── DELETE JOB ──────────────────────────────────
@login_required
def delete_job(request, pk):
    job = get_object_or_404(JobApplication, pk=pk, user=request.user)
    if request.method == 'POST':
        job.delete()
        messages.success(request, "Job deleted!")
    return redirect('job_list')
