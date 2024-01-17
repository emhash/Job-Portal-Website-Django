from django.shortcuts import render,get_object_or_404
from .models import CreateJobPost

def job_details(request, id):
    the_post = get_object_or_404(CreateJobPost, uid = id)
    context = {
        "the_post":the_post
    }
    return render(request, "home/pages/job_detail.html", context)