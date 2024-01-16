from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib import messages


def user_login(request):
    return render(request, "home/pages/login.html")

def user_register(request):
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Congrats your registration is done!")
            return redirect("homepage")
        
    else:
        form = UserForm()

    context = {
        "form":form,
    }
    return render(request, "home/pages/register.html", context)
