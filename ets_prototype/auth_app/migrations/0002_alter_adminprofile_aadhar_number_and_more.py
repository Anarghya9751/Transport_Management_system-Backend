# Generated by Django 5.0.6 on 2024-07-18 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminprofile',
            name='aadhar_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='adminprofile',
            name='contact_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='aadhar_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='contact_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='driverprofile',
            name='aadhar_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='driverprofile',
            name='contact_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='employeeprofile',
            name='aadhar_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='employeeprofile',
            name='contact_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='vendorprofile',
            name='aadhar_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='vendorprofile',
            name='contact_number',
            field=models.IntegerField(),
        ),
    ]