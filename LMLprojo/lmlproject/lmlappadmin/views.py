from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
# from lmlappadmin.models import *
from .models import *

@login_required()
def home(request):
    context={
        'title': 'Dash',
    }
    return render(request,'admin/index.html', context)

@login_required()
def employee_messages(request):
    context = {
        'title': 'Messages',
    }
    return render(request, 'messages/employee.html', context)

@login_required()
def company_messages(request):
    context = {
        'title': 'Messages',
    }
    return render(request, 'messages/company.html', context)

@login_required()
def employees(request):
    context = {
        'title': 'Employees',
    }
    return render(request,'employee/allemployees.html', context)

@login_required()
def companies(request):
    company = Company.objects.all()
    print(company)
    context = {
        'title': 'Companies',
        'companies': company,
    }
    return render(request, 'company/company.html', context)

@login_required()
def categories(request):
    context = {
        'title': 'Categories',
    }
    return render(request, 'categories/categories.html',context)