from django.urls import path, include
from . import views

urlpatterns = [
    path("employee/", views.emp_dashboard, name="dashboard"),
    path("employee/checkpoint-and-setup/", views.confirm_employee_profile, name="confirm_employee_profile"),
    path("checkpoint/<str:the_id>", views.set_employe_profile, name="set_employe_profile")
]