from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'LML'
urlpatterns = [
    path('', views.home, name="home"),
    path('signup/', views.signup_initial, name="signup_initial"),
    path('signupcompany/', views.signup_company_initial, name="signup_company_initial"),
    path('signupemployee/', views.signup_employee_initial, name="signup_employee_initial"),

    path('loginauser/<str:source>/', views.login_user, name="login_user"),
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

    path('employer/user_account/change_password', views.employer_change_password, name='employer_change_password'),

    path('companypricing/', views.companypricing, name="companypricing"),
    path('contactus/', views.contactus, name="contactus"),

    path('termsandconditons/', views.termsandconditons, name="termsandconditons"),
    path('FAQ/', views.frequentaskedquestions, name="frequentaskedquestions"),

    path('companycontactus/',views.company_contact_us, name='company_contact_us'),
    path('homecontactus/<str:source>',views.home_contact_us, name='home_contact_us'),

    path('payment/',views.payment, name='payment'),
    path('companypayment/',views.companypayment, name='companypayment'),
    path('companypaymentpackage/<int:pricing_id>',views.companypaymentpackage, name='companypaymentpackage'),
    path('employerdash/',views.employer_dash, name='employer_dash'),

    # employeestatus
    path('allpremiumemployees/',views.all_premium_employees, name = 'all_premium_employees'),
    path('allemployees/',views.all_employees, name = 'all_employees'),
    path('premiumemployeedetails/<int:customer_id>', views.premium_employee_details, name='premium_employee_detail'),

    path('shortlist/', views.shortlistcustomers, name='shortlistemployees'),
    path('categories/', views.categories, name='viewcategories'),

]