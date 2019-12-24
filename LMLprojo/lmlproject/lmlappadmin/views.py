from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
import sweetify
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
def random_messages(request):
    contactushome = ContactUsHome.objects.order_by("-created_at")
    context = {
        'title': 'Random Messages',
        'messages':contactushome,
        'messagecount':contactushome.count(),
        'inboxcount': ContactUsHome.objects.filter(status="UNREAD").count()
    }
    return render(request, 'messages/RandomMessages.html', context)

@login_required()
def company_messages(request):
    context = {
        'title': 'Messages',
    }
    return render(request, 'messages/company.html', context)

@login_required()
def employees(request):
    employees = Customer.objects.order_by('-created_at')
    context = {
        'title': 'Employees',
        'customers': employees,
    }
    return render(request,'employee/allemployees.html', context)

@login_required()
def premiumemployees(request):
    employees = Customer.objects.filter(rank_status='PREMIUM').order_by('-created_at')
    context = {
        'title': 'PremiumEmployees',
        'customers': employees,
    }
    return render(request,'employee/premiumemployees.html', context)

@login_required()
def shortlistedemployees(request):

     # = Customer.objects.filter(rank_status='PREMIUM').order_by('-created_at')
    # customers =[]
    employ = CompanyShortlistCustomers.objects.filter()
    context = {
        'title': 'ShortlistedEmployees',
        'customers': employ,
    }
    return render(request,'employee/shortlistedemployies.html', context)

@login_required()
def registeredemployees(request):

    employ = Customer.objects.filter(regpayment_id__isnull=False)
    context = {
        'title': 'RegisteredEmployees',
        'customers': employ,
    }
    return render(request,'employee/registeredemployees.html', context)

@login_required()
def deactivatedemployees(request):

    employ = Customer.objects.filter(status='DEACTIVATED')
    context = {
        'title': 'DeactivatedEmployees',
        'customers': employ,
    }
    return render(request,'employee/deactivatedemployees.html', context)



@login_required()
def companies(request):
    company = Company.objects.all()

    context = {
        'title': 'Companies',
        'companies': company,
    }
    return render(request, 'company/company.html', context)

@login_required()
def premiumcompanies(request):
    company = Company.objects.filter(rank_status='PREMIUM')

    context = {
        'title': 'Premium Companies',
        'companies': company,
    }
    return render(request, 'company/premiumcompanies.html', context)

@login_required()
def platinumcompanies(request):
    company = Company.objects.filter(rank_status='PLATINUM')

    context = {
        'title': 'Platinum Companies',
        'companies': company,
    }
    return render(request, 'company/platinumcompanies.html', context)

@login_required()
def basiccompanies(request):
    company = Company.objects.filter(rank_status='BASIC')

    context = {
        'title': 'Basic Companies',
        'companies': company,
    }
    return render(request, 'company/basiccompanies.html', context)

@login_required()
def probasiccompanies(request):
    company = Company.objects.filter(rank_status='PRO_BASIC')

    context = {
        'title': 'Probasic Companies',
        'companies': company,
    }
    return render(request, 'company/probasiccompanies.html', context)


@login_required()
def proultimatecompanies(request):
    company = Company.objects.filter(rank_status='PRO_ULTIMATE')

    context = {
        'title': 'Probasic Companies',
        'companies': company,
    }
    return render(request, 'company/proultimatecompanies.html', context)

@login_required()
def ultimatecompanies(request):
    company = Company.objects.filter(rank_status='ULTIMATE')

    context = {
        'title': 'Ultimate Companies',
        'companies': company,
    }
    return render(request, 'company/ultimatecompany.html', context)

@login_required()
def undefinedcompanies(request):
    company = Company.objects.filter(rank_status='UNDEFINED')

    context = {
        'title': 'Undefined Companies',
        'companies': company,
    }
    return render(request, 'company/undefinedcompanies.html', context)

@login_required()
def companiesregpayment(request):
    company = Company.objects.filter(regpayment_id__isnull=False)

    context = {
        'title': 'Company Registration Payment',
        'companies': company,
    }
    return render(request, 'company/registrationpayment.html', context)

def deactivatedemployers(request):
    company = Company.objects.filter(status='DEACTIVATED')

    context = {
        'title': 'Deactivated Company',
        'companies': company,
    }
    return render(request, 'company/deactivatedcompanies.html', context)





def companyPricing(request):
    pricing = CompanyPricingPlan.objects.all()
    if request.method == 'POST':
        title = request.POST['title']
        price = request.POST['price']
        description = request.POST['description']
        CompanyPricingPlan.objects.create(
            title=title,
            price=price,
            description=description
        )
        sweetify.success(request, 'Success', text='Price Added', persistent='Ok')
    else:
        pricing = CompanyPricingPlan.objects.all()


    context = {
        'title': 'Companies Pricing',
        'pricings': pricing

    }
    return render(request, 'company/companypricing.html', context)


@login_required()
def categories(request):
    categories = Category.objects.all()
    context = {
        'title': 'Categories',
        'categories': categories,
    }
    return render(request, 'categories/categories.html',context)


def carouselImages(request):
    if request.method == 'POST':
        image = request.FILES['carousel_image']
        img = AdvertCarousel.objects.create(
            carousel_image=image
        )
        if img:
            sweetify.success(request, 'Success', text='Advert Added Successfully', persistent='Ok')
            return redirect('LMLAdmin:carouselImages')
        else:
            sweetify.error(request, 'Error', text='Error adding', persistent='Retry')
            return redirect('LMLAdmin:carouselImages')

    context = {
        'title': 'Categories',
        'images': AdvertCarousel.objects.order_by('-created_at'),
    }
    return render(request, 'advertimages/carouselimages.html', context)