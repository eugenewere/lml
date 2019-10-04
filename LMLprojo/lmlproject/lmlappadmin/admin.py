from django.contrib import admin
from lmlappadmin.models import *
# Register your models here.


admin.site.register(County)
admin.site.register(Region)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Employer)
admin.site.register(Query)
admin.site.register(Reply)
admin.site.register(Contacts)
admin.site.register(CustomerPayments)
admin.site.register(EmployerPayments)

