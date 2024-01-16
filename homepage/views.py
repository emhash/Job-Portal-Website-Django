from django.shortcuts import render,redirect,get_list_or_404
from employee.models import JobCategory, CreateJobPost, EmployeeProfile

def index(request):
    category = JobCategory.objects.all()
    jobs = CreateJobPost.objects.all()
    context = {
        "categories":category,
        "jobs":jobs,
    }
    return render(request, "home/pages/index.html", context)