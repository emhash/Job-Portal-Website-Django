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
            self.fields['name'].label = "Enter your own name"
            self.fields['document'].label = "Your legal valid document (If want to provide)"
                 

class CompanyForm(forms.ModelForm):
    stablished_at = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Company
        fields = "__all__"
        exclude = ['first_employee','secret_key']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control border-1 bg-light px-4',
                'style':"height: 55px;",
                'placeholder': self.fields[field].label if self.fields[field].label else '',
                })
            self.fields['document'].label = "Provide legal any document of your company (if have)"
