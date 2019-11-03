from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'LML'
urlpatterns = [
    path('', views.home, name="home"),
    path('signup/', views.signup_initial, name="signup_initial"),

    path('loginauser/', views.login_user, name="login_user"),
    path('logoutuser/', views.log_out_user, name="log_out_user"),

    path('personelsignup/', views.signup, name="signup"),
    path('companysignup/', views.companysignup, name="companysignup"),
    path('companysignup/formhandling/', views.company_signupform_handling, name="company_signup_formhandling"),

    path('signin/', views.signin, name="signin"),

    path('employeeprofile/', views.employeeprofile, name="employeeprofile"),
    path('employeedetails/', views.employeedetails, name="employeedetails"),
    path('advancesearch/', views.advancesearch, name="advancesearch"),

    path('employersprofile/', views.employersprofile, name="employersprofile"),
    path('updateemployersprofile/', views.update_employers_profile, name="update_employers_profile"),
    path('employerdetails/', views.employerdetails, name="employerdetails"),

    path('companypricing/', views.companypricing, name="companypricing"),
    path('contactus/', views.contactus, name="contactus"),
]