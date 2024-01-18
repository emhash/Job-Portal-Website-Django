from django import forms 
from .models import JobApplications

class JobApplicationsForm(forms.ModelForm):
    
    class Meta:
        model = JobApplications
        fields = "__all__"
        exclude = ['job_seeker', 'job']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control bg-light border-1',
                'style':"height: 35px;",
                'placeholder': self.fields[field].label if self.fields[field].label else '',
                })