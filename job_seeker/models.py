from django.db import models
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
    job_seeker = models.ForeignKey(JobSeekerProfile, on_delete=models.CASCADE)
    upload_cv = models.FileField(upload_to="ApplicantCVs")
    job = models.ForeignKey("employee.CreateJobPost", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.job_seeker} : {self.job}"
    