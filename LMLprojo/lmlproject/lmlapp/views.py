import csv

import io
import requests
import urllib3
import json
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse
from django.shortcuts import render, redirect,HttpResponseRedirect
import os

import sweetify
from django.utils.crypto import get_random_string

from lmlapp.forms import *
from .models import *
import base64

# Create your views here.

# # Base method with no type specified
# sweetify.sweetalert(self.request, 'Westworld is awesome', text='Really... if you have the chance - watch it!' persistent='I agree!')
#
# # Additional methods with the type already defined
# sweetify.info(self.request, 'Message sent', button='Ok', timer=3000)
# sweetify.success(self.request, 'You successfully changed your password')
# sweetify.error(self.request, 'Some error happened here - reload the site', persistent=':(')
# sweetify.warning(self.request, 'This is a warning... I guess')
import json

def home(request):



    context = {
        'title': 'home',
        'counties': County.objects.all(),
        'categories':Category.objects.all(),
    }
    return render(request, 'normal/home/index.html', context)


def signup(request):

    if request.method=='POST':
        qualifications = request.POST.getlist('qualifications[]')
        schools = request.POST.getlist('school[]')
        courses = request.POST.getlist('course[]')
        graduation_dates = request.POST.getlist('graduation_date[]')
        regnos = request.POST.getlist('reg_number[]')


        employer_names = request.POST.getlist('employer_name[]')
        company_names = request.POST.getlist('company_name[]')
        company_emails = request.POST.getlist('company_email[]')
        company_phones = request.POST.getlist('company_phone[]')
        position_helds = request.POST.getlist('position_held[]')
        date_froms = request.POST.getlist('date_from[]')
        date_tos = request.POST.getlist('date_to[]')
        experiences = request.POST.getlist('experience[]')

        skills = request.POST.getlist('skill[]')
        referees = request.POST.getlist('referee[]')
        referee_phonenumbers= request.POST.getlist('referee_phonenumber[]')

        account_url= request.POST['account_url']



        form = PersonelRegisterForm(request.POST, request.FILES)
        # print(form)
        if form.is_valid():
            new_user= form.save()
            CustomerRegNo.objects.create(
                customer=new_user,
                personel_reg_no=get_random_string(length=7, allowed_chars='PERS123456789'),
            )
            Social_account.objects.create(
                customer=new_user,
                account_url=account_url
            )
            for skill in skills:
                for referee in referees:
                    for referee_phonenumber in referee_phonenumbers:
                        if skills.index(skill) == referees.index(referee) and skills.index(skill) == referee_phonenumbers.index(referee_phonenumber):
                            Skills.objects.create(
                                customer=new_user,
                                skill= skill,
                                referee=referee,
                                referee_phonenumber=referee_phonenumber
                            )
            # print(qualifications)
            # print(schools)
            # print(courses)
            # print(regnos)
            # print(graduation_dates)
            for qualification in qualifications:
                for school in schools:
                    for course in courses:
                        for graduation_date in graduation_dates:
                            for regno in regnos:
                                if qualifications.index(qualification) == schools.index(school) and qualifications.index(qualification) == courses.index(course) \
                                        and qualifications.index(qualification) == graduation_dates.index(graduation_date) and qualifications.index(qualification) == regnos.index(regno):
                                    Education.objects.create(
                                        customer=new_user,
                                        qualifications=qualification,
                                        school=school,
                                        course=course,
                                        graduation_date=graduation_date,
                                        reg_number=regno,
                                    )
                                    print(qualification)

            for employer_name in employer_names:
                for company_name in company_names:
                    for company_email in company_emails:
                        for company_phone in company_phones:
                            for position_held in position_helds:
                                for date_from in date_froms:
                                    for date_to in date_tos:
                                        for experience in experiences:
                                            if employer_names.index(employer_name) == company_names.index(company_name) and employer_names.index(employer_name) == company_emails.index(company_email) \
                                                and employer_names.index(employer_name) == company_phones.index(company_phone) and employer_names.index(employer_name) == position_helds.index(position_held)\
                                                and employer_names.index(employer_name) == date_froms.index(date_from) and employer_names.index(employer_name) == date_tos.index(date_to) \
                                                and employer_names.index(employer_name) == experiences.index(experience):
                                                Experience.objects.create(
                                                    customer=new_user,
                                                    employer_name=employer_name,
                                                    company_name=company_name,
                                                    comapny_email=company_email,
                                                    company_phone=company_phone,
                                                    position_held = position_held,
                                                    date_from=date_from,
                                                    date_to=date_to,
                                                    experience=experience,
                                                )


            sweetify.success(request, 'You did it', text='Good job! You successfully Registered', persistent='Continue')
        else:
            form1 = PersonelRegisterForm(request.POST,request.FILES)
            sweetify.error(request, 'Error', text='Error Registering your account', persistent='Retry')
            return render(request, 'normal/signup/signup.html',{'form':form1})




    module_dir = os.path.dirname(__file__)  # get current directory
    file_path1 = os.path.join(module_dir, 'Bachelorcourses')
    file_path2 = os.path.join(module_dir, 'course_certificate')
    file_path3 = os.path.join(module_dir, 'DiplomaCourses')
    file_path4 = os.path.join(module_dir, 'phdcourses')
    file_path5 = os.path.join(module_dir, 'Masterscourses')
    file_path6 = os.path.join(module_dir, 'university')
    # file_path6 = os.path.join(module_dir, 'categories')
    qbfile = open(file_path1, "r")
    qbfile2 = open(file_path2, "r")
    qbfile3 = open(file_path3, "r")
    qbfile4 = open(file_path4, "r")
    qbfile5 = open(file_path5, "r")
    qbfile6 = open(file_path6, "r")




    context = {
        'title': 'Create an account',
        'bachelors':qbfile.readlines(),
        'certificates':qbfile2.readlines(),
        'diplomas':qbfile3.readlines(),
        'phds':qbfile4.readlines(),
        'masters':qbfile5.readlines(),
        'unis':qbfile6.readlines(),
        'counties':County.objects.all(),
        'regions':Region.objects.all(),
        'categories':Category.objects.all(),
        # 'universities':qbfile6.readlines(),




    }
    return render(request, 'normal/signup/signup.html',context)

def company_signupform_handling(request):

    # company_name = request.POST.get('company_name')
    # company_email = request.POST.get('company_email')
    # company_motto = request.POST.get('company_motto')
    # category = request.POST.get('category')
    # bizness_entity_type = request.POST.get('bizness_entity_type')
    # website = request.POST.get('website')
    # bussiness_reg_no = request.POST.get('bussiness_reg_no')
    # county = request.POST.get('county')
    # description = request.POST.get('description')
    # region = request.POST.get('region')
    # landmark = request.POST.get('landmark')
    # brief_details = request.POST.get('brief_details')
    # kra_number = request.POST.get('kra_number')
    # date_created = request.POST.get('date_created')
    # logo = request.FILES.get('logo')
    #
    # first_name = request.POST.get('first_name')
    # last_name = request.POST.get('last_name')
    # email = request.POST.get('email')
    # username = request.POST.get('username')


        return redirect('LML:companysignup' )
        # return redirect('LML:companysignup')

def update_employers_profile(request):
    user= request.user.id

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')

        facebook = request.POST.get('facebook')
        googlr_plus = request.POST.get('googlr_plus')
        twitter = request.POST.get('twitter')
        instagram = request.POST.get('instagram')
        linkedin = request.POST.get('linkedin')
        company = Company.objects.filter(id=request.user.id).first()
        form = CompanyUserupdateForm(request.POST, request.FILES, instance=company)
        print(form)
        if form.is_valid():
            updated=form.save()
            CompanySocialAccount.objects.filter(company=company.id).update(
                company=updated,
                facebook=facebook,
                googlr_plus=googlr_plus,
                twitter=twitter,
                instagram=instagram,
                linkedin=linkedin,
            )
            User.objects.filter(pk=request.user.id).update(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username
            )
            sweetify.success(request, 'Success', text='Good job! You successfully Updated Your Account', persistent='Ok')
            return redirect('LML:employerdetails')
        else:

            sweetify.error(request, 'Error', text='Error updating your account', persistent='Retry')
            return redirect('LML:employersprofile')
            # return redirect('LML:companysignup',{'form':formr})
    else:
        return redirect('LML:employersprofile')


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




def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']


        def usernamel(email):
            uz = User.objects.filter(email__exact=email).first()
            # us = User.objects.filter(email=uz.email).values('username').first()
            print(uz.email)
            print(uz.username)

            if uz.email:
                return uz.username
            return None

        if User.objects.filter(username__exact=username).first() or User.objects.filter(email__exact=username).first():
            if User.objects.filter(username__exact=username).first():

                user=authenticate(request, username=username, password=password)
                if user is not None:
                    if user.is_staff and user.is_active:
                        login(request, user)
                        sweetify.success(request, title='Welcome Admin', text='Welcome Back', persistent='Continue')
                        return redirect('LMLAdmin:home')
                    if user.is_active:
                        if Company.objects.filter(user_ptr_id=user.id).exists():
                            login(request, user)
                            sweetify.success(request, title='Welcome to Labour Market Link', text='You successfully Logged in.', persistent='Continue')
                            return redirect('LML:employerdetails')
                        if Customer.objects.filter(user_ptr_id=user.id).exists():
                            login(request, user)
                            sweetify.success(request, title='Welcome to Labour Market Link', text='You successfully Logged in.', persistent='Continue')
                            return redirect('LML:employeedetails')
                else:
                    sweetify.error(request, 'Error', text='Invalid Username and Password', persistent='Retry')
                    return redirect('LML:signin')
                    # return render(request, 'normal/login/login.html', {'username': username, })

            if User.objects.filter(email__exact=username).first():

                user = authenticate(request, username=usernamel(username), password=password)
                if user is not None:
                    if user.is_staff and user.is_active:
                        login(request, user)
                        sweetify.success(request, title='Welcome Admin', text='Welcome Back', persistent='Continue')
                        return redirect('LMLAdmin:home')
                    if user.is_active:
                        if Company.objects.filter(user_ptr_id=user.id).exists():
                            login(request, user)
                            sweetify.success(request, title='Welcome to Labour Market Link',
                                             text='You successfully Logged in.', persistent='Continue')
                            return redirect('LML:employerdetails')
                        if Customer.objects.filter(user_ptr_id=user.id).exists():
                            login(request, user)
                            sweetify.success(request, title='Welcome to Labour Market Link',
                                             text='You successfully Logged in.', persistent='Continue')
                            return redirect('LML:employeedetails')
                else:
                    sweetify.error(request, 'Error', text='Invalid Email and Password', persistent='Retry')
                    return redirect('LML:signin')
                    # return render(request, 'normal/login/login.html', {'username': username, })
        else:
            sweetify.error(request, 'Error', text='Invalid Credentials dont exist', persistent='Retry')
            return redirect('LML:signin')
    return render(request, 'normal/login/login.html')


def signin(request):
    return render(request, 'normal/login/loginstyled.html')

def log_out_user(request):
    logout(request)
    return redirect('LML:signin')

def employer_change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            sweetify.success(request, title='Success', text='Password Changed.', persistent='Continue')
            return redirect("LML:employersprofile")
        else:
            form = PasswordChangeForm(request.user)
            sweetify.error(request, 'Error', text='Password not Changed', persistent='Retry')
            return render(request, 'normal/account/employer-profile.html', {'form':form})
    else:
        form = PasswordChangeForm(request.user)
        return redirect("LML:employersprofile")


@login_required()
def employerdetails(request):
    user = request.user
    company = Company.objects.filter(id=user.id).first()
    social = CompanySocialAccount.objects.filter(company=company.id).first()
    similar_company = Company.objects.filter(category=company.category)
    context = {
       'company':company,
       'social': social,
       'scompany': similar_company,
    }
    return render(request ,'normal/jobdetails/employerdetails.html', context)

@login_required()
def employersprofile(request):
    user = request.user
    company = Company.objects.filter(id=user.id).first()
    social = CompanySocialAccount.objects.filter(company=company.id).first()
    similar_company = Company.objects.filter(category=company.category).exclude(id=user.id)
    categories = Category.objects.all()
    # social = CompanySocialAccount.objects.filter(company=company.id).first()
    kenyan_county_api_url = "https://raw.githubusercontent.com/mikelmaron/kenya-election-data/master/data/counties.geojson"
    kenyan_constituencies_api_url = "https://raw.githubusercontent.com/mikelmaron/kenya-election-data/master/data/constituencies.geojson"

    data = requests.get(kenyan_county_api_url).json()
    data2 = requests.get(kenyan_constituencies_api_url).json()
    context = {
        'title': 'Company profile',
        'user': request.user,
        'company':company,
        'social':social,
        'scompany':similar_company,
        'categories':categories,
        'counties': data['features'],
        'regions': data2['features'],
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
    facebook = request.POST.get('facebook')
    googlr_plus = request.POST.get('googlr_plus')
    twitter = request.POST.get('twitter')
    instagram = request.POST.get('instagram')
    linkedin = request.POST.get('linkedin')

    if request.method == 'POST':
        # form = CompanyUserSignUpForm(request.POST)
        form = CompanyRegisterForm(request.POST, request.FILES)
        form2 = CompanySocialsForm(request.POST)

        # print(form)
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
            CompanyRegNo.objects.create(
                company=new_user,
                company_reg_no=get_random_string(length=7, allowed_chars='COMP123456789'),
            )
            sweetify.success(request, 'You did it', text='Good job! You successfully registered', persistent='Ok')
            return redirect('LML:signin')
        else:
            # formr = CompanyRegisterForm()
            # print(formr.errors)
            sweetify.error(request, 'Error', text='Ensure you fill all fields correctly', persistent='Retry')
            return render(request, 'normal/signup/create-company.html', {'form': form, 'social': form2})
            # return redirect('LML:companysignup',{'form':form, 'social':form2})

    else:

        form = CompanyRegisterForm()
        form2 = CompanySocialsForm()
        categories = Category.objects.all()





    context = {
        'title': 'Create an account',
         'counties':County.objects.all(),
        'regions':Region.objects.all(),
        'categories': categories,
        'form': form,
        'social': form2,


    }

    return render(request, 'normal/signup/create-company.html', context)


def advancesearch(request):
    context={
        'title':"Advance search",
        'categories': Category.objects.all(),
    }
    return render(request, 'normal/advancedsearch/advancedsearch.html', context)




def companypricing(request):
    context={
        'title':'Company Pricing',
    }
    return render(request,'normal/companypricing/companypricing.html', context)


def contactus(request):
    context={
        'title':'Contact Us',
    }
    return render(request,'normal/contact/contact.html', context)


def signup_initial(request):
    context={
        'title': "Signup",
    }
    return render(request, 'normal/signup/signupdecision.html', context)


def termsandconditons(request):
    context={
        'title':'Terms and Conditions',
    }
    return render(request, 'normal/termsandconditions/terms.html', context)


def frequentaskedquestions(request):
    context={
        'title':'FAQ',
    }
    return render(request, 'normal/faq/faq.html', context)


def signup_employee_initial(request):
    context={
        'title':'Employee Signup',
    }
    return render(request, 'normal/signup/employeesignupdecision.html', context )


def signup_company_initial(request):
    context={
        'title':'Company Signup',
    }
    return render(request, 'normal/signup/companysignupdecision.html', context)


def company_contact_us(request):
    user = request.user.id
    company = Company.objects.filter(user_ptr_id = user).first()
    name = request.POST['name']
    email = request.POST['email']
    message = request.POST['message']
    if request.method =='POST':
        ContactUsCompany.objects.create(
          name=name,
          company=company,
          email=email,
          message=message,
        )
        sweetify.success(request, 'Success', text='Message sent', persistent='Ok')
        return redirect('LML:employerdetails')
    else:
        sweetify.success(request, 'Error', text='Message not sent', persistent='Ok')
    return redirect('LML:employerdetails')


def payment(request):
    return render(request,'normal/payment/payment-method.html')


def employer_dash(request):
    return render(request,'normal/employer-dash/employer-dash.html')