from django.contrib import admin
from .models import EmployeeProfile,CompanyProfile,JobCategory,CreateJobPost
# Register your models here.
admin.site.register(EmployeeProfile)
admin.site.register(CompanyProfile)
admin.site.register(JobCategory)
admin.site.register(CreateJobPost)