from django.shortcuts import render,redirect,get_object_or_404
from employee.models import EmployeeProfile,Company, CompanyProfile
from users.models import Profile
from django.contrib import messages
from employee.forms import EmployeeProfileForm,CompanyForm



def set_employe_profile(request,the_id):
    profile = request.user.profile
    the_company = get_object_or_404(Company, uid = the_id.strip())

    get_emp, created = EmployeeProfile.objects.get_or_create(account = profile)
    if request.method == "POST":
        form = EmployeeProfileForm(request.POST,request.FILES, instance = get_emp)
        if form.is_valid():
            form.instance.is_set = True
            form.save()
            the_employe = form.instance

            existing_profile = CompanyProfile.objects.filter(
                            institute=the_company,
                            personal_emplyee=the_employe
                        ).first()

            if not existing_profile:
                # Create CompanyProfile object only if it doesn't exist
                company_profile = CompanyProfile.objects.create(
                    institute=the_company,
                    personal_emplyee=form.instance
                )


            messages.success(request,"Your profile set success!")
            return redirect("homepage")
    else:
        form = EmployeeProfileForm(instance = get_emp)


    context = {
        "form":form,
    }
    return render(request, "home/pages/confirm_register.html", context)


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
                elif privet_key:
                    print(request.POST.get('privet_key').strip() )
                    
                elif selected_company:
                    the_id = request.POST.get('selected_company').strip()
                    return redirect("set_employe_profile", the_id = the_id)
                                                            

                else:
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
            saved_company = form1.instance  
            saved_employee = form.instance 

            existing_profile = CompanyProfile.objects.filter(
                institute=form1.instance,
                personal_emplyee=form.instance
            ).first()

            if not existing_profile:
                # Create CompanyProfile object only if it doesn't exist
                company_profile = CompanyProfile.objects.create(
                    institute=form1.instance,
                    personal_emplyee=form.instance,
                    approved = True
                )

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