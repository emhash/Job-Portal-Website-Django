from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index , name="homepage"),
    path('jobs/', views.job_list , name="job_list"),
    
    path('details/<str:id>/', views.job_details , name="job_details"),
    
   
]