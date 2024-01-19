from django.shortcuts import render,redirect,get_object_or_404
from employee.models import EmployeeProfile,Company, CompanyProfile
from users.models import Profile
from django.contrib import messages
from employee.forms import EmployeeProfileForm,CompanyForm

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
                    the_company = get_object_or_404(Company, uid = request.POST.get('selected_company').strip())
                    print(the_company)
                    
                    if request.method == "POST":
                        pass
                    else:
                        employe = EmployeeProfile()

                    return redirect(request.path)

            context={
                'all_company':all_company,
            }
            return render(request, "home/pages/confirm_profile.html", context)
        else:
            return render(request, "dashboard/employee/index.html")
    else:
        return redirect("homepage")



def confirm_employee_profile(request):
    profile = get_object_or_404(Profile, user = request.user)
    ep, created = EmployeeProfile.objects.get_or_create(account=profile)
    # the_instance 
    c_instance = Company.objects.filter(first_employee = ep).first()

    if request.method == "POST":
            
        form1 = CompanyForm(request.POST, request.FILES, instance = c_instance)
        form = EmployeeProfileForm(request.POST, request.FILES, instance=ep)
        if form.is_valid() and form1.is_valid():
            form.instance.account = profile
            form.instance.is_set = True
            form1.instance.first_employee = ep
            form.save()
            form1.save()
            

            messages.success(request, "Personal information saved!")
            return redirect("homepage")
        

        
    else:
        form = EmployeeProfileForm(instance=ep)
        form1 = CompanyForm(instance = c_instance)
    context = {
        "form": form,
        "form1": form1,
        
    }
    return render(request, "home/pages/confirm_register.html", context)