from django.db import models
import uuid
from ckeditor.fields import RichTextField

'''
Job Listings:	
Employers can create job listings by providing details such as 
job title, 
description, 
requirements, and 
location.

Job listings should display key information, such as 
the job title,
company name, and 
date posted.

'''

'''

Job Categories: 
Jobs can be categorized based on 
industries, 
making it easier for users to find relevant listings.

'''

class CommonBaseModel(models.Model):
    uid = models.UUIDField(primary_key=True, default= uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class EmployeeProfile(CommonBaseModel):
    name = models.CharField( max_length=450)
    document = models.FileField(upload_to="Employee-Validity-Check-Doc/" , blank=True, null= True)

    def __str__(self) -> str:
        return f"{self.name}"


class CompanyProfile(CommonBaseModel):
    personal_emplyee = models.ForeignKey(EmployeeProfile, on_delete=models.CASCADE)
    brand_logo = models.FileField(upload_to="LogoOfCompanies")

class JobCategory(CommonBaseModel):
    name = models.CharField( max_length=150)
    tags = models.TextField(null=True, blank=True) #Need to provide tag separate by comma

    def __str__(self):
        return self.name
    

class CreateJobPost(CommonBaseModel):
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    category = models.ForeignKey(JobCategory, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=250)
    description = RichTextField()
    requirements = RichTextField()
    location = models.CharField(max_length=450)
    vacancy = models.PositiveIntegerField()
    salary_range_start = models.PositiveIntegerField()
    salary_range_end = models.PositiveIntegerField()

    deadline = models.DateField(auto_now=False, auto_now_add=False)
    
    def __str__(self):
        return self.job_title
    
    
# ========----------- JOB POST PART END -----------===========


'''


User Dashboard: 
Employers have a dashboard to manage their posted job listings, 
view applications, and update job details.

'''
