from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from lmlappadmin.models import *
from django import forms

class CompanyUserSignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email','first_name','last_name','password2', 'password1','username']

class CompanyOtherDetailForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['logo','company_name', 'company_email', 'company_motto', 'category', 'bizness_entity_type', 'website','bussiness_reg_no','county', 'region','landmark','brief_details', 'date_created', 'description', 'kra_number']

class CompanySocialsForm(forms.ModelForm):
    class Meta:
        model = CompanySocialAccount
        fields = ['facebook','linkedin', 'googlr_plus', 'instagram', 'twitter', 'company' ]



class CompanyRegisterForm(forms.Form, UserCreationForm):
    first_name =forms.CharField(
                    max_length=30,
                    widget=forms.TextInput(
                        attrs={
                            'placeholder': 'Company Name',
                            'class':'form-control',

                        }
                    )
                )
    class Meta:
        model = Company
        fields = ['email','first_name','last_name','password2', 'password1','username','logo','company_name', 'company_email', 'company_motto', 'category', 'bizness_entity_type', 'website','bussiness_reg_no','county', 'region','landmark','brief_details', 'date_created', 'description', 'kra_number',]

    def clean_username(self, *args, **kwargs):
        super(CompanyRegisterForm, self).clean()
        username = self.cleaned_data.get('username')
        if User.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError('Username already exists')
        return username

    def clean_email(self, *args, **kwargs):
        super(CompanyRegisterForm, self).clean()
        email = self.cleaned_data.get('email')
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError('A user has already registered using this email')
        return email

    def clean_password2(self, *args, **kwargs):
        super(CompanyRegisterForm, self).clean()
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords must match')
        return password2

 # def clean_date_of_birth(self):
    #     '''
    #     Only accept users aged 13 and above
    #     '''
    #     userAge = 13
    #     dob = self.cleaned_data.get('date_of_birth')
    #     today = date.today()
    #     if (dob.year + userAge, dob.month, dob.day) > (today.year, today.month, today.day):
    #         raise forms.ValidationError('Users must be aged {} years old and above.'.format(userAge))
    #     return dob