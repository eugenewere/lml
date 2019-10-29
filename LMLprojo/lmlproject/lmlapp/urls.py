from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'LML'
urlpatterns = [
    path('', views.home, name="home"),
    path('personelsignup/', views.signup, name="signup"),
    path('companysignup/', views.companysignup, name="companysignup"),
    path('signin/', views.signin, name="signin"),

    path('employeeprofile/', views.employeeprofile, name="employeeprofile"),
    path('employeedetails/', views.employeedetails, name="employeedetails"),
    path('advancesearch/', views.advancesearch, name="advancesearch"),

    path('employersprofile/', views.employersprofile, name="employersprofile"),
    path('employerdetails/', views.employerdetails, name="employerdetails"),

    path('companypricing/', views.companypricing, name="companypricing"),
    path('contactus/', views.contactus, name="contactus"),
]