from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'LMLAdmin'
urlpatterns = [
    path('',views.home,name='home'),
    path('messages/employee/',views.employee_messages ,name='E_messages'),
    path('messages/company/',views.company_messages, name='C_messages'),
    path('allemployees/',views.employees, name='employees'),
    path('allcompanies/',views.companies, name='companies'),
    path('companyPricing/',views.companyPricing, name='companyPricing'),
    path('allcategories/',views.categories, name='categories'),
]