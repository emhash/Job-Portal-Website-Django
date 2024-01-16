from .models import User
from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

class UserForm(UserCreationForm):
    ROLE_CHOICES = [        
        ('employee', 'Employee'),
        ('job_seekers', 'Job Seekers'),
    ]

    role = forms.ChoiceField(choices=ROLE_CHOICES, label='Role')
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['email','role', 'password1', 'password2']




    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
    
        if not email:
            raise forms.ValidationError("Please provide a valid email.")
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control border-1 bg-light px-4',
                'style':"height: 55px;",
                'placeholder': self.fields[field].label if self.fields[field].label else '',
                })