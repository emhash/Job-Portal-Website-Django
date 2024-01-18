from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout, login

from .forms import UserForm


def user_login(request):
    return render(request, "home/pages/login.html")

def user_register(request):
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.save()
            login(request, new_user)  
            messages.success(request, "Congrats your registration is done!")
            return redirect("homepage")
        
    else:
        form = UserForm()

    context = {
        "form":form,
    }
    return render(request, "home/pages/register.html", context)
