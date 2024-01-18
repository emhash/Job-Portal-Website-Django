from django.shortcuts import render,redirect,get_object_or_404
from employee.models import JobCategory, CreateJobPost, EmployeeProfile

def index(request):
    category = JobCategory.objects.all()
    jobs = CreateJobPost.objects.all()[:20] # Here need to mixed up with different categories jobs.
    
    full_time_jobs = CreateJobPost.objects.filter(full_time = True).order_by("-created_at")[:12]
    part_time_jobs = CreateJobPost.objects.filter(full_time = False).order_by("-created_at")[:12]

    context = {
        "categories":category,
        "jobs":jobs,
        "full_time_jobs":full_time_jobs,
        "part_time_jobs":part_time_jobs,
    }
    return render(request, "home/pages/index.html", context)


def job_list(request):

    category = JobCategory.objects.all()
    jobs = CreateJobPost.objects.all()[:40] # Here need to mixed up with different categories jobs.
    
    full_time_jobs = CreateJobPost.objects.filter(full_time = True).order_by("-created_at")[:30]
    part_time_jobs = CreateJobPost.objects.filter(full_time = False).order_by("-created_at")[:30]

    context = {
        "categories":category,
        "jobs":jobs,
        "full_time_jobs":full_time_jobs,
        "part_time_jobs":part_time_jobs,
    }

    return render(request, "home/pages/job_list.html", context)


def job_details(request, id):
    the_post = get_object_or_404(CreateJobPost, uid = id)
    context = {
        "the_post":the_post
    }
    return render(request, "home/pages/job_detail.html", context)