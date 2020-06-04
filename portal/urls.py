from django.urls import path
from .import views

urlpatterns = [

    path('', views.home, name='home'),
    path('register/', views.registerpage, name='register'),
    path('adminregister/', views.adminregisterpage, name='register'),
    path('employerregister/', views.employerregisterpage, name='register'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('joblist/<int:pk_test>', views.joblist, name='joblist'),
    path('profile/', views.profilepage, name='profile'),
    path('applyjob/<int:pk>', views.applyjob, name='apply_job'),
    path('backend/', views.get_backends, name='get_backends'),
]