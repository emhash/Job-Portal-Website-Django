from django.db import models
from users.models import Profile

import uuid

'''

Job seekers have a dashboard to track their applications,
 and update their profiles.

'''


class CommonBaseModel(models.Model):
    uid = models.UUIDField(primary_key=True, default= uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


GENDERS = [
        ('male', 'male'),       
        ('female', 'female'),       
        ]

class JobSeekerProfile(CommonBaseModel):
    name = models.CharField( max_length=450)
    date_of_birth = models.DateField( auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=50, choices=GENDERS)
    address = models.CharField( max_length=550)

    # More details like education can be add here  

    def __str__(self):
        return self.name
    

class JobApplications(CommonBaseModel):
    name = models.CharField( max_length=150, null=True, blank=True)
    job_seeker = models.ForeignKey(Profile, on_delete=models.CASCADE)
    upload_cv = models.FileField(upload_to="ApplicantCVs")
    job = models.ForeignKey("employee.CreateJobPost", on_delete=models.CASCADE)
    
    portfolio = models.CharField( max_length=550, null=True, blank=True)
    cover_letter = models.TextField(null=True, blank= True)
    def __str__(self):
        return f"{self.job_seeker} : {self.job}"
    