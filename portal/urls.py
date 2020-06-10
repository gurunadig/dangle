from django.urls import path
from .import views

urlpatterns = [

    path('', views.home, name='home'),
    path('register/', views.registerpage, name='register'),
    path('adminregister/', views.adminregisterpage, name='adminregister'),
    path('employerregister/', views.employerregisterpage, name='employerregister'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('joblist/<int:pk_test>', views.joblist, name='joblist'),
    path('jobdetails/', views.jobdetails, name='jobdetails'),
    # path('profile/', views.profilepage, name='profile'),
    path('applyjob/<int:pk>', views.applyjob, name='apply_job'),
    path('backend/', views.get_backends, name='get_backends'),

    # here starts admin urls 
    path('adminpanel/', views.adminpanel, name='adminpanel'),
    path('addjobs/', views.addjobs, name='addjobs'),
    path('updatejobs/<int:pk>', views.updatejobs, name='updatejobs'),
    path('deletejobs/<int:pk>', views.deletejobs, name='deletejobs'),
    path('appliedjobs/', views.appliedjobs, name='appliedjobs'),
    path('candidatesearch/', views.candidatesearch, name='candidatesearch'),
    path('profilelist/', views.profilelist, name='profilelist'),
]