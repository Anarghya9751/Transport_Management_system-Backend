# Generated by Django 5.0.6 on 2024-07-18 10:17

import django.db.models.deletion
import trip_management_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth_app', '0002_alter_adminprofile_aadhar_number_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route_id', models.CharField(default=trip_management_app.models.generate_vehicle_id, max_length=20)),
                ('origin_latitude', models.FloatField()),
                ('origin_longitude', models.FloatField()),
                ('destination_latitude', models.FloatField()),
                ('destination_longitude', models.FloatField()),
                ('distance', models.FloatField()),
                ('duration', models.FloatField()),
                ('status', models.CharField(choices=[('active', 'Active'), ('busy', 'Busy'), ('inactive', 'Inactive')], default='active', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Vehicle_id', models.CharField(default=trip_management_app.models.generate_vehicle_id, max_length=20)),
                ('vehicle_type', models.CharField(choices=[('car', 'Car'), ('van', 'Van'), ('bus', 'Bus'), ('other', 'Other')], max_length=20)),
                ('capacity', models.IntegerField(max_length=10)),
                ('status', models.CharField(choices=[('active', 'Active'), ('busy', 'Busy'), ('inactive', 'Inactive')], default='active', max_length=20)),
                ('last_maintenance_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trip_id', models.CharField(default=trip_management_app.models.generate_vehicle_id, max_length=20)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('scheduled', 'Scheduled'), ('completed', 'Completed'), ('cancelled', 'Cancelled')], default='pending', max_length=20)),
                ('driver_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth_app.driverprofile')),
                ('route_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trip_management_app.route')),
                ('vehicle_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trip_management_app.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='TransportRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_date', models.DateTimeField(auto_now_add=True)),
                ('scheduled_date', models.DateTimeField()),
                ('type', models.CharField(choices=[('pickup', 'Pickup'), ('dropoff', 'Dropoff')], max_length=20)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected'), ('completed', 'Completed')], max_length=50)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth_app.employeeprofile')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trip_management_app.vehicle')),
            ],
        ),
    ]
