# Generated by Django 5.0.7 on 2024-07-27 11:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0003_alter_customuser_role_commanderprofile'),
        ('bill_report_app', '0002_alter_bill_bill_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='company_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='auth_app.companyprofile'),
        ),
    ]
