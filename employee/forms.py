from django import forms 
from .models import EmployeeProfile,Company

class EmployeeProfileForm(forms.ModelForm):
    
    class Meta:
        model = EmployeeProfile
        fields = "__all__"
        exclude = [ 'account', 'is_set']

        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control border-1 bg-light px-4',
                'style':"height: 55px;",
                'placeholder': self.fields[field].label if self.fields[field].label else '',
                })     

class CompanyForm(forms.ModelForm):
    
    class Meta:
        model = Company
        fields = "__all__"
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control border-1 bg-light px-4',
                'style':"height: 55px;",
                'placeholder': self.fields[field].label if self.fields[field].label else '',
                })
