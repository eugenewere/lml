from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.db import models
from datetime import datetime
import datetime

# Create your models here.
class County(models.Model):
    county = models.CharField(max_length=200,null=False,blank=False)
    l_parent = models.ForeignKey('County', related_name='location_county', on_delete=models.CASCADE, max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % (self.county)
    
class Region(models.Model):
    region = models.CharField(max_length=200,null=False,blank=False)
    county = models.ForeignKey(County, on_delete=models.CASCADE, max_length=200, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % (self.region)

class Category(models.Model):
    category = models.CharField(max_length=200, null=False, blank=False)
    c_parent = models.ForeignKey('Category', related_name='job_category', on_delete=models.CASCADE, max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % (self.category)

class Customer(get_user_model()):
    profile_image = models.ImageField(max_length=200, upload_to='customerImages', null=False, blank=False)
    county = models.ForeignKey(County, on_delete=models.CASCADE,max_length=200, null=False, blank=False)
    region = models.ForeignKey(Region, on_delete=models.CASCADE,max_length=200, null=False, blank=False)
    gender = models.CharField(max_length=100,null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, max_length=200, null=False, blank=False)
    skils =  models.CharField(max_length=100,null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    years_of_experience = models.CharField(max_length=100,null=False, blank=False)
    ref_no = models.CharField(max_length=100, null=False, blank=False, unique=True)
    date_of_birth = models.DateField(default=datetime.datetime.now())
    huduma_no = models.CharField(max_length=100,null=True, blank=True)
    marital_status = models.CharField(max_length=100,null=True, blank=True)
    driver_licence = models.CharField(max_length=100,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'


class Employer(get_user_model()):
    logo = models.ImageField(max_length=200, upload_to='employerlogo', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, max_length=200, null=False, blank=False)
    company_name = models.CharField(max_length=200, null=True, blank=True)
    huduma_no = models.CharField(max_length=100, null=True, blank=True)
    # kra_pin = models.
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
    bussiness_no = models.CharField(max_length=100,null=True, blank=True,unique=True, validators=[alphanumeric])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    class Meta:
        verbose_name = 'Employer'
        verbose_name_plural = 'Employers'

class Query(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=False, blank=False)
    content = models.TextField()

    QUERYSTATUS = {
        ('READ','Read'),
        ('UNREAD','Unread'),
        ('TRASH', 'Trash'),

    }
    status = models.CharField(choices=QUERYSTATUS, default='UNREAD', max_length=100,null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s %s' % (self.customer, self.status)


class Reply(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=False, blank=False)
    query = models.ForeignKey(Query, on_delete=models.CASCADE, null=False, blank=False)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % (self.customer)

class Contacts(models.Model):
    email=models.CharField(max_length=200, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    address = models.CharField(max_length=200, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s %s (%s)' % (self.email, self.phone_number, (self.address))

class CustomerPayments(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=False, blank=False)
    amount = models.FloatField()
    paid_to = models.CharField(max_length=200, null=True, blank=True)
    paid_date = models.DateField(default=datetime.datetime.now())
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s %s' % (self.customer, self.amount)

class EmployerPayments(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=False, blank=False)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE, null=False, blank=False)
    amount = models.FloatField()
    paid_to = models.CharField(max_length=200, null=True, blank=True)
    paid_date = models.DateField(default=datetime.datetime.now())
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s (%s) %s' % (self.employer, (self.customer), self.amount)

