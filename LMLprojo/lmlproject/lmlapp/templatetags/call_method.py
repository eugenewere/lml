import statistics
from datetime import date

from django import template
from django.shortcuts import render_to_response
from django.views import View
from lmlappadmin.models import *


register = template.Library()

@register.filter(name='logged_in_company')
def logged_in_company(user):
    user_id = user.id
    company = Company.objects.filter(user_ptr_id=user_id).first()
    if company is not None:
        return company
    else:
        return False

@register.filter(name='logged_in_customer')
def logged_in_customer(user):
    user_id = user.id
    customer = Customer.objects.filter(user_ptr_id=user_id).first()
    if customer is not None:
        return customer
    else:
        return False

@register.filter(name='make_safe')
def make_safe(source):
    source = source.replace('/', '____')
    return "%s" %source

@register.filter(name='today')
def today(request):
    user = request.user.id
    today = date.today()
    # company = Company.objects.filter(user_ptr_id = user).first()
    # experience = ( (today.strftime("%Y")) - company.date_created)
    return today

@register.filter(name='experience_years')
def experience_years(experience_id):
    experience = Experience.objects.filter(id=experience_id).first()
    date_from = experience.date_from
    date_to = experience.date_to
    diff = date_to-date_from
    if diff.days > 365:
        day = str(int(diff.days/365)) + str(' Years')
        return day
    elif diff.days < 365:
        day = str(int(diff.days/30)) + str(' Monthes')
        return day
    else:
        return 0

