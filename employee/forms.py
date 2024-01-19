from django import forms 
from .models import EmployeeProfile,Company

class EmployeeProfileForm(forms.ModelForm):
    
    class Meta:
        model = EmployeeProfile
        fields = "__all__"
        exclude = [ 'account', 'is_set']
        

class CompanyForm(forms.ModelForm):
    
    class Meta:
        model = Company
        fields = "__all__"
        

