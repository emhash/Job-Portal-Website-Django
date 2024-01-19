from django.shortcuts import render,redirect,get_object_or_404
from employee.models import EmployeeProfile,Company, CompanyProfile
from django.contrib import messages

def emp_dashboard(request):
    if request.user.role == "employee":
        profile = request.user.profile
        get_or_create = EmployeeProfile.objects.get_or_create(account = profile)
        
        employee_profile = get_object_or_404(EmployeeProfile, account = profile)
        
        if not employee_profile.is_set:
            all_company = Company.objects.all()
            if request.method == "POST":
                privet_key = request.POST.get('privet_key')
                selected_company = request.POST.get('selected_company')
                if privet_key and selected_company:
                    messages.warning(request, "Go back and reload the page and try again!")
                    return redirect(request.path)
                else:
                    print(request.POST.get('privet_key'))
                    print(request.POST.get('selected_company'))
                    return redirect(request.path)

            context={
                'all_company':all_company,
            }
            return render(request, "home/pages/confirm_profile.html", context)
        else:
            return render(request, "dashboard/employee/index.html")
    else:
        return redirect("homepage")


from employee.forms import EmployeeProfileForm,CompanyForm

def confirm_employee_profile(request):
    profile = request.user.profile
    ep = EmployeeProfile.objects.get_or_create(account = profile)
    form = EmployeeProfileForm(instance=profile)
    form1 = CompanyForm()
    context = {
        "form":form,
        "form1":form1,
    }
    return render(request,"home/pages/confirm_register.html", context)