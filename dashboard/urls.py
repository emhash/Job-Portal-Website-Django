from django.urls import path, include
from . import views

urlpatterns = [
    path("employee/", views.emp_dashboard, name="dashboard"),
    path("employee/company-profile-set/", views.confirm_employee_profile, name="confirm_employee_profile"),
]