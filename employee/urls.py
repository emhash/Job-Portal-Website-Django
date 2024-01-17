from django.urls import path, include
from . import views

urlpatterns = [
    path('details/<str:id>/', views.job_details , name="job_details"),
    

   
]