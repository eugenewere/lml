from django.shortcuts import render

# Create your views here.
def home(request):
    context={
        'title': 'Dash',
    }
    return render(request,'admin/index.html', context)


def employee_messages(request):
    context = {
        'title': 'Messages',
    }
    return render(request, 'messages/employee.html', context)


def company_messages(request):
    context = {
        'title': 'Messages',
    }
    return render(request, 'messages/company.html', context)


def employees(request):
    context = {
        'title': 'Employees',
    }
    return render(request,'employee/allemployees.html', context)


def companies(request):
    context = {
        'title': 'Companies',
    }
    return render(request, 'company/company.html', context)


def categories(request):
    context = {
        'title': 'Categories',
    }
    return render(request, 'categories/categories.html',context)