# Generated by Django 2.1.7 on 2019-11-13 22:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lmlappadmin', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='driver_licence',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='skils',
        ),
        migrations.AddField(
            model_name='customer',
            name='disability_status',
            field=models.CharField(choices=[('DISABLED', 'Disabled'), ('NOT_DISABLED', 'Not_Disabled')], default='NOT_DISABLED', max_length=200),
        ),
        migrations.AddField(
            model_name='education',
            name='graduation_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 14, 1, 16, 48, 129495)),
        ),
        migrations.AddField(
            model_name='education',
            name='reg_number',
            field=models.CharField(default=2233, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='company',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2019, 11, 14, 1, 16, 48, 129495)),
        ),
        migrations.AlterField(
            model_name='company',
            name='status',
            field=models.CharField(choices=[('PREMIUM', 'Premium'), ('REGISTERED_CONFIRMED', 'Registerd_confirmed'), ('DEACTIVATED', 'Deactivated'), ('NEWBIE', 'Newbie')], default='NEWBIE', max_length=200),
        ),
        migrations.AlterField(
            model_name='customer',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2019, 11, 14, 1, 16, 48, 123970)),
        ),
        migrations.AlterField(
            model_name='customer',
            name='landmark',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='status',
            field=models.CharField(choices=[('PREMIUM', 'Premium'), ('REGISTERED_CONFIRMED', 'Registerd_confirmed'), ('DEACTIVATED', 'Deactivated'), ('NEWBIE', 'Newbie')], default='NEWBIE', max_length=200),
        ),
        migrations.AlterField(
            model_name='customerpayments',
            name='paid_date',
            field=models.DateField(default=datetime.datetime(2019, 11, 14, 1, 16, 48, 142040)),
        ),
        migrations.AlterField(
            model_name='employerpayments',
            name='paid_date',
            field=models.DateField(default=datetime.datetime(2019, 11, 14, 1, 16, 48, 142040)),
        ),
        migrations.AlterField(
            model_name='experience',
            name='comapny_email',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='company_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='company_phone',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='date_from',
            field=models.DateField(default=datetime.datetime(2019, 11, 14, 1, 16, 48, 129495)),
        ),
        migrations.AlterField(
            model_name='experience',
            name='date_to',
            field=models.DateField(default=datetime.datetime(2019, 11, 14, 1, 16, 48, 129495)),
        ),
        migrations.AlterField(
            model_name='experience',
            name='employer_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='position_held',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='query',
            name='status',
            field=models.CharField(choices=[('READ', 'Read'), ('TRASH', 'Trash'), ('UNREAD', 'Unread')], default='UNREAD', max_length=100),
        ),
    ]