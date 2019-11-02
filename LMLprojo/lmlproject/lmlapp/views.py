import json
import urllib

import requests
import urllib3
from django.shortcuts import render, redirect
import os
import sweetify

from lmlapp.forms import *
from .models import *


# Create your views here.

# # Base method with no type specified
# sweetify.sweetalert(self.request, 'Westworld is awesome', text='Really... if you have the chance - watch it!' persistent='I agree!')
#
# # Additional methods with the type already defined
# sweetify.info(self.request, 'Message sent', button='Ok', timer=3000)
# sweetify.success(self.request, 'You successfully changed your password')
# sweetify.error(self.request, 'Some error happened here - reload the site', persistent=':(')
# sweetify.warning(self.request, 'This is a warning... I guess')


def home(request):
    # sweetify.success(request, 'You did it', text='Good job! You successfully showed a SweetAlert message', persistent='Hell yeah')
    context = {
        'title': 'home',
    }
    return render(request, 'normal/home/index.html', context)


def signup(request):
    # sweetify.error(request, 'You did it', text='Good job! You successfully showed a SweetAlert message', persistent='Hell yeah')
    module_dir = os.path.dirname(__file__)  # get current directory
    file_path1 = os.path.join(module_dir, 'Bachelorcourses')
    file_path2 = os.path.join(module_dir, 'course_certificate')
    file_path3 = os.path.join(module_dir, 'DiplomaCourses')
    qbfile = open(file_path1, "r")
    qbfile2 = open(file_path2, "r")
    qbfile3 = open(file_path3, "r")

    # response = requests.get('https://africaopendata.org/dataset/a8f8b195-aafd-449b-9b1a-ab337fd9925f/resource/4fb2e27e-c001-4b7f-b71d-4fee4a96a0f8/download/kenyan-counties.geojson')
    # geodata = response.json()

    kenyan_county_api_url ="https://raw.githubusercontent.com/mikelmaron/kenya-election-data/master/data/counties.geojson"
    kenyan_constituencies_api_url ="https://raw.githubusercontent.com/mikelmaron/kenya-election-data/master/data/constituencies.geojson"

    data=requests.get(kenyan_county_api_url).json()
    data2=requests.get(kenyan_constituencies_api_url).json()

    # for county in data['features']:
    # 4db8ff



    context = {
        'title': 'Create an account',
        'bachelors':qbfile.readlines(),
        'certificates':qbfile2.readlines(),
        'diplomas':qbfile3.readlines(),
        'counties':data['features'],
        'regions':data2['features'],



    }
    return render(request, 'normal/signup/signup.html',context)

def company_signupform_handling(request):

    company_name = request.POST.get('company_name')
    company_email = request.POST.get('company_email')
    company_motto = request.POST.get('company_motto')
    category = request.POST.get('category')
    bizness_entity_type = request.POST.get('bizness_entity_type')
    website = request.POST.get('website')
    bussiness_reg_no = request.POST.get('bussiness_reg_no')
    county = request.POST.get('county')
    description = request.POST.get('description')
    region = request.POST.get('region')
    landmark = request.POST.get('landmark')
    brief_details = request.POST.get('brief_details')
    kra_number = request.POST.get('kra_number')
    date_created = request.POST.get('date_created')
    logo = request.FILES.get('logo')

    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')
    username = request.POST.get('username')

    facebook = request.POST.get('facebook')
    googlr_plus = request.POST.get('googlr_plus')
    twitter = request.POST.get('twitter')
    instagram = request.POST.get('instagram')
    linkedin = request.POST.get('linkedin')


    if request.method == 'POST':
        # form = CompanyUserSignUpForm(request.POST)
        form = CompanyRegisterForm(request.POST, request.FILES)
        # form2 = CompanyOtherDetailForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            new_user = form.save()
            CompanySocialAccount.objects.create(
                company=new_user,
                facebook=facebook,
                googlr_plus=googlr_plus,
                twitter=twitter,
                instagram=instagram,
                linkedin=linkedin,
            )
            sweetify.success(request, 'You did it', text='Good job! You successfully registered', persistent='Ok')
            return redirect('LML:companysignup')
        else:
            formr = CompanyRegisterForm()
            print(formr.errors)
            sweetify.error(request, 'Error', text='Ensure you fill all fields correctly', persistent='Retry')
            return render(request, 'normal/signup/create-company.html', {'form':formr, 'categories': Category.objects.all(),})
            # return redirect('LML:companysignup',{'form':formr})
    else:
        formr = CompanyRegisterForm()
        return redirect('LML:companysignup')

    # context = {
    #     'logo': logo,
    #     'company_name': company_name,
    #     'company_email': company_email,
    #     'company_motto': company_motto,
    #     'categoryy': category,
    #     'bizness_entity_type': bizness_entity_type,
    #     'website': website,
    #     'bussiness_reg_no': bussiness_reg_no,
    #     'county': county,
    #     'regiont': region,
    #     'landmark': landmark,
    #     'brief_details': brief_details,
    #     'date_created': date_created,
    #     'first_name': first_name,
    #     'last_name': last_name,
    #     'email': email,
    #     'facebook': facebook,
    #     'googlr_plus': googlr_plus,
    #     'twitter': twitter,
    #     'instagram': instagram,
    #     'linkedin': linkedin,
    #     'description': description,
    #     'kra_number': kra_number,
    #     'username': username,
    # }







def signin(request):
    return render(request, 'normal/login/login.html')


def employersprofile(request):
    sweetify.success(request, 'You did it', text='Good job! You successfully showed a SweetAlert message', persistent='Hell yeah')

    context = {
        'title': 'Company profile',
    }
    return render(request, 'normal/account/employer-profile.html',context)


def employeeprofile(request):
    context = {
        'title': 'Your Profile',
    }
    return render(request, 'normal/account/candidate-profile.html', context)


def employeedetails(request):
    return render(request, 'normal/account/candidate-detail.html')


def companysignup(request):
    kenyan_county_api_url = "https://raw.githubusercontent.com/mikelmaron/kenya-election-data/master/data/counties.geojson"
    kenyan_constituencies_api_url = "https://raw.githubusercontent.com/mikelmaron/kenya-election-data/master/data/constituencies.geojson"

    data = requests.get(kenyan_county_api_url).json()
    data2 = requests.get(kenyan_constituencies_api_url).json()

    context = {
        'title': 'Create an account',
        'counties': data['features'],
        'regions': data2['features'],
        'categories': Category.objects.all(),


    }

    return render(request, 'normal/signup/create-company.html', context)


def advancesearch(request):
    return render(request, 'normal/advancedsearch/advancedsearch.html')


def employerdetails(request):
    return render(request ,'normal/jobdetails/employerdetails.html')


def companypricing(request):
    return render(request,'normal/companypricing/companypricing.html')


def contactus(request):
    return render(request,'normal/contact/contact.html')


def signup_initial(request):
    return render(request, 'normal/signup/signupdecision.html')


