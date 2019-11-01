from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from lmlappadmin.models import *
from django import forms

class CompanyUserSignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email','first_name','last_name','password2', 'password1']

class CompanyOtherDetailForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['logo','company_name', 'company_email', 'company_motto', 'category', 'bizness_entity_type', 'website','bussiness_reg_no','county', 'region','landmark','brief_details', 'date_created', 'description', 'kra_number']

class CompanySocialsForm(forms.ModelForm):
    class Meta:
        model = CompanySocialAccount
        fields = ['facebook','linkedin', 'googlr_plus', 'instagram', 'twitter', 'company' ]
