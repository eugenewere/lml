# Generated by Django 2.1.15 on 2020-01-05 07:42

import datetime
from django.conf import settings
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvertCarousel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carousel_image', models.ImageField(max_length=250, upload_to='home_couresel')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('c_parent', models.ForeignKey(blank=True, max_length=200, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='job_category', to='lmlappadmin.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('logo', models.ImageField(blank=True, max_length=200, null=True, upload_to='employerlogo')),
                ('company_name', models.CharField(max_length=200)),
                ('phone_number', models.CharField(default='0700000000', max_length=200)),
                ('landmark', models.CharField(max_length=100)),
                ('company_motto', models.CharField(max_length=100)),
                ('brief_details', models.TextField()),
                ('bizness_entity_type', models.CharField(max_length=100)),
                ('date_created', models.DateField(default=datetime.datetime.now)),
                ('description', models.TextField()),
                ('website', models.CharField(blank=True, max_length=100, null=True)),
                ('company_email', models.CharField(max_length=100)),
                ('kra_number', models.CharField(max_length=100)),
                ('bussiness_reg_no', models.CharField(blank=True, max_length=100, null=True, unique=True, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('NEWBIE', 'Newbie'), ('DEACTIVATED', 'Deactivated'), ('REGISTERED_CONFIRMED', 'Registerd_confirmed')], default='NEWBIE', max_length=200)),
                ('rank_status', models.CharField(choices=[('PLATINUM', 'Platinum'), ('PRO_BASIC', 'Pro_basic'), ('ULTIMATE', 'Ultimate'), ('BASIC', 'Basic'), ('UNDEFINED', 'Undefined'), ('PRO_ULTIMATE', 'Pro_ultimate'), ('PREMIUM', 'Premium')], default='UNDEFINED', max_length=200)),
                ('category', models.ForeignKey(max_length=200, on_delete=django.db.models.deletion.CASCADE, to='lmlappadmin.Category')),
            ],
            options={
                'verbose_name': 'Employer',
                'verbose_name_plural': 'Employers',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='CompanyPricingPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CompanyRegistrationPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipt_no', models.CharField(max_length=200)),
                ('amount', models.CharField(max_length=200)),
                ('payment_status', models.CharField(choices=[('UNPAYED', 'Unpayed'), ('PAYED', 'Payed')], default='UNPAYED', max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyRegNo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_reg_no', models.CharField(max_length=100, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lmlappadmin.Company')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyShortlistCustomers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lmlappadmin.Company')),
            ],
        ),
        migrations.CreateModel(
            name='CompanySocialAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.CharField(blank=True, max_length=200, null=True)),
                ('googlr_plus', models.CharField(blank=True, max_length=200, null=True)),
                ('twitter', models.CharField(blank=True, max_length=200, null=True)),
                ('linkedin', models.CharField(blank=True, max_length=200, null=True)),
                ('instagram', models.CharField(blank=True, max_length=200, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lmlappadmin.Company')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyStatusPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipt_no', models.CharField(max_length=200)),
                ('amount', models.CharField(max_length=200)),
                ('payment_status', models.CharField(choices=[('UNPAYED', 'Unpayed'), ('PAYED', 'Payed')], default='UNPAYED', max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lmlappadmin.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContactUsCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lmlappadmin.Company')),
            ],
        ),
        migrations.CreateModel(
            name='ContactUsEmployee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContactUsHome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(blank=True, choices=[('TRASH', 'Trash'), ('READ', 'Read'), ('UNREAD', 'Unread')], default='UNREAD', max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('county_number', models.IntegerField()),
                ('county', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('profile_image', models.ImageField(blank=True, max_length=200, null=True, upload_to='customerImages')),
                ('country', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('date_of_birth', models.DateField(default=datetime.datetime.now)),
                ('landmark', models.CharField(blank=True, max_length=100, null=True)),
                ('huduma_no', models.CharField(blank=True, max_length=100, null=True)),
                ('job_type', models.CharField(max_length=200)),
                ('disability', models.TextField(blank=True, null=True)),
                ('marital_status', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('biography', models.TextField()),
                ('status', models.CharField(choices=[('NEWBIE', 'Newbie'), ('DEACTIVATED', 'Deactivated'), ('REGISTERED_CONFIRMED', 'Registerd_confirmed')], default='NEWBIE', max_length=200)),
                ('rank_status', models.CharField(choices=[('PREMIUM', 'Premium'), ('ULTIMATE', 'Ultimate'), ('BASIC', 'Basic')], default='BASIC', max_length=200)),
                ('disability_status', models.CharField(choices=[('DISABLED', 'Disabled'), ('NOT_DISABLED', 'Not_Disabled')], default='NOT_DISABLED', max_length=200, null=True)),
                ('category', models.ForeignKey(max_length=200, on_delete=django.db.models.deletion.CASCADE, to='lmlappadmin.Category')),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lmlappadmin.County')),
            ],
            options={
                'verbose_name': 'Customer',
                'verbose_name_plural': 'Customers',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='CustomerPayments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('recipt_no', models.CharField(max_length=200)),
                ('payment_status', models.CharField(choices=[('UNPAYED', 'Unpayed'), ('PAYED', 'Payed')], default='UNPAYED', max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerRegNo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personel_reg_no', models.CharField(max_length=100, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lmlappadmin.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerReviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('ratings', models.IntegerField(blank=True, default=0, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lmlappadmin.Company')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lmlappadmin.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualifications', models.CharField(max_length=200)),
                ('school', models.CharField(max_length=200)),
                ('course', models.CharField(max_length=200)),
                ('graduation_date', models.DateTimeField(default=datetime.datetime(2020, 1, 5, 10, 42, 56, 41181))),
                ('reg_number', models.CharField(max_length=200)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lmlappadmin.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='EmployerPayments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('paid_to', models.CharField(blank=True, max_length=200, null=True)),
                ('paid_date', models.DateField(default=datetime.datetime.now)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lmlappadmin.Customer')),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lmlappadmin.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employer_name', models.CharField(blank=True, max_length=200, null=True)),
                ('company_name', models.CharField(blank=True, max_length=200, null=True)),
                ('comapny_email', models.CharField(blank=True, max_length=200, null=True)),
                ('company_phone', models.CharField(blank=True, max_length=200, null=True)),
                ('position_held', models.CharField(blank=True, max_length=200, null=True)),
                ('date_from', models.DateField(default=datetime.datetime.now)),
                ('date_to', models.DateField(default=datetime.datetime.now)),
                ('experience', models.TextField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lmlappadmin.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg_content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(blank=True, choices=[('TRASH', 'Trash'), ('READ', 'Read'), ('UNREAD', 'Unread')], default='UNREAD', max_length=200, null=True)),
                ('reciever', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reciever', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('status', models.CharField(choices=[('TRASH', 'Trash'), ('READ', 'Read'), ('UNREAD', 'Unread')], default='UNREAD', max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lmlappadmin.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('county_number', models.IntegerField()),
                ('region', models.CharField(max_length=200)),
                ('ward', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lmlappadmin.Customer')),
                ('query', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lmlappadmin.Query')),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=100)),
                ('referee', models.CharField(max_length=100)),
                ('referee_phonenumber', models.CharField(max_length=100)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lmlappadmin.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Social_account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_url', models.CharField(max_length=100)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lmlappadmin.Customer')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lmlappadmin.Region'),
        ),
        migrations.AddField(
            model_name='customer',
            name='regpayment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lmlappadmin.CustomerPayments'),
        ),
        migrations.AddField(
            model_name='contactusemployee',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lmlappadmin.Customer'),
        ),
        migrations.AddField(
            model_name='companyshortlistcustomers',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lmlappadmin.Customer'),
        ),
        migrations.AddField(
            model_name='company',
            name='county',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lmlappadmin.County'),
        ),
        migrations.AddField(
            model_name='company',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lmlappadmin.Region'),
        ),
        migrations.AddField(
            model_name='company',
            name='regpayment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lmlappadmin.CompanyRegistrationPayment'),
        ),
    ]
