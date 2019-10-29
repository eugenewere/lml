import json
import urllib

import requests
import urllib3
from django.shortcuts import render
import os

# Create your views here.



def home(request):
    context = {
        'title': 'home',
    }
    return render(request, 'normal/home/index.html', context)


def signup(request):

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




    context = {
        'title': 'Create an account',
        'bachelors':qbfile.readlines(),
        'certificates':qbfile2.readlines(),
        'diplomas':qbfile3.readlines(),
        'counties':data['features'],
        'regions':data2['features']
    }
    return render(request, 'normal/signup/signup.html',context)


def signin(request):
    return render(request, 'normal/login/login.html')


def employersprofile(request):
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
    return render(request, 'normal/signup/create-company.html')


def advancesearch(request):
    return render(request, 'normal/advancedsearch/advancedsearch.html')


def employerdetails(request):
    return render(request ,'normal/jobdetails/employerdetails.html')


def companypricing(request):
    return render(request,'normal/companypricing/companypricing.html')


def contactus(request):
    return render(request,'normal/contact/contact.html')