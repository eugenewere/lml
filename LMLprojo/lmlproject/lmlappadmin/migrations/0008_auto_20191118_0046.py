# Generated by Django 2.1.11 on 2019-11-17 21:46

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lmlappadmin', '0007_merge_20191118_0044'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUsCompany',
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
        migrations.AlterField(
            model_name='company',
            name='date_created',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='company',
            name='status',
            field=models.CharField(choices=[('REGISTERED_CONFIRMED', 'Registerd_confirmed'), ('DEACTIVATED', 'Deactivated'), ('PREMIUM', 'Premium'), ('NEWBIE', 'Newbie')], default='NEWBIE', max_length=200),
        ),
        migrations.AlterField(
            model_name='customer',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='customer',
            name='status',
            field=models.CharField(choices=[('REGISTERED_CONFIRMED', 'Registerd_confirmed'), ('DEACTIVATED', 'Deactivated'), ('PREMIUM', 'Premium'), ('NEWBIE', 'Newbie')], default='NEWBIE', max_length=200),
        ),
        migrations.AlterField(
            model_name='customerpayments',
            name='paid_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='education',
            name='graduation_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 18, 0, 46, 14, 344225)),
        ),
        migrations.AlterField(
            model_name='employerpayments',
            name='paid_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='experience',
            name='date_from',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='experience',
            name='date_to',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='query',
            name='status',
            field=models.CharField(choices=[('TRASH', 'Trash'), ('UNREAD', 'Unread'), ('READ', 'Read')], default='UNREAD', max_length=100),
        ),
        migrations.AddField(
            model_name='contactusemployee',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lmlappadmin.Company'),
        ),
        migrations.AddField(
            model_name='contactuscompany',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lmlappadmin.Company'),
        ),
    ]