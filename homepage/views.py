from django.shortcuts import render,redirect,get_object_or_404
from employee.models import JobCategory, CreateJobPost, EmployeeProfile
from django.contrib import messages


from job_seeker.forms import JobApplicationsForm



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



# @login_required()
def job_details(request, id):
    the_post = get_object_or_404(CreateJobPost, uid = id)
    if request.method == "POST":
        form = JobApplicationsForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.job_seeker = request.user.profile
            form.instance.job = the_post

            form.save()
            messages.success(request, "Congrats! your application sumbitted successfully.")
            return redirect("homepage")
    else:
        form = JobApplicationsForm()

    context = {
        "the_post":the_post,
        "form":form,
    }
    return render(request, "home/pages/job_detail.html", context)