from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'LML'
urlpatterns = [
    path('', views.home, name="home"),
    path('signup/', views.signup, name="signup"),
    path('signin/', views.signin, name="signin"),
    path('employersprofile/', views.employersprofile, name="employersprofile"),
    path('employeeprofile/', views.employeeprofile, name="employeeprofile"),
    path('employeedetails/', views.employeedetails, name="employeedetails"),
]