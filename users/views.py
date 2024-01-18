from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout, login

from .forms import UserForm

def user_login(request):
    if request.method == "POST":
        user_email = request.POST.get('user_email')
        user_password = request.POST.get('user_password')

        # Authenticate the user
        user = authenticate(request, username=user_email, password=user_password)

        if user is not None:
            login(request, user)
            messages.success(request, "Log in successful!")
            return redirect("homepage")
        else:
            messages.warning(request, "Invalid email or password.")

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


def user_logout(request):
    logout(request)
    messages.warning(request, "You have been logged out!")
    return redirect("homepage")