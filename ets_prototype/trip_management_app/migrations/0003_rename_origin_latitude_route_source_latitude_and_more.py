# Generated by Django 5.0.6 on 2024-07-23 12:02

import django.db.models.deletion
import trip_management_app.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0003_alter_customuser_role_commanderprofile'),
        ('trip_management_app', '0002_alter_vehicle_capacity'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='route',
            old_name='origin_latitude',
            new_name='source_latitude',
        ),
        migrations.RenameField(
            model_name='route',
            old_name='origin_longitude',
            new_name='source_longitude',
        ),
        migrations.RemoveField(
            model_name='transportrequest',
            name='vehicle',
        ),
        migrations.AddField(
            model_name='transportrequest',
            name='trip',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='trip_management_app.trip'),
        ),
        migrations.AddField(
            model_name='trip',
            name='end_latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='trip',
            name='end_longitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='trip',
            name='start_latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='trip',
            name='start_longitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='route',
            name='route_id',
            field=models.CharField(default=trip_management_app.models.generate_route_id, max_length=20),
        ),
        migrations.AlterField(
            model_name='trip',
            name='trip_id',
            field=models.CharField(default=trip_management_app.models.generate_trip_id, max_length=20),
        ),
        migrations.CreateModel(
            name='OtherRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('escort', 'Escort'), ('multiple_day_trip', 'Multiple Day Trip'), ('on_demand', 'On Demand')], max_length=20)),
                ('guest_name', models.TextField()),
                ('guest_contact_number', models.IntegerField()),
                ('request_date', models.DateTimeField(auto_now_add=True)),
                ('scheduled_time', models.DateTimeField()),
                ('source_latitude', models.FloatField()),
                ('source_longitude', models.FloatField()),
                ('destination_latitude', models.FloatField()),
                ('destination_longitude', models.FloatField()),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('scheduled', 'Scheduled'), ('completed', 'Completed'), ('cancelled', 'Cancelled')], default='pending', max_length=20)),
                ('start_latitude', models.FloatField()),
                ('start_longitude', models.FloatField()),
                ('end_latitude', models.FloatField()),
                ('end_longitude', models.FloatField()),
                ('days', models.IntegerField()),
                ('driver_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth_app.driverprofile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vehicle_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trip_management_app.vehicle')),
            ],
        ),
    ]
