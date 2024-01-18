from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.user_login, name="user_login" ),
    path('register/', views.user_register, name="user_register" ),
    path('logout/', views.logout, name="user_logout"),

]