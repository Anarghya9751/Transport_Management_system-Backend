from django.db.models.signals import post_save
from .models import CustomUser, AdminProfile, CommanderProfile, VendorProfile, CompanyProfile, DriverProfile, EmployeeProfile
from django.dispatch import receiver


@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    # if created:
    #     Profile.objects.create(user=instance)
    if created:
        if instance.role == "admin":
            AdminProfile.objects.create(user=instance)
        elif instance.role == "commander":
            CommanderProfile.objects.create(user=instance)
        elif instance.role == "vendor":
            VendorProfile.objects.create(user=instance)
        elif instance.role == "company":
            CompanyProfile.objects.create(user=instance)
        elif instance.role == "driver":
            DriverProfile.objects.create(user=instance)
        elif instance.role == "employee":
            EmployeeProfile.objects.create(user=instance)
    


# @receiver(post_save, sender=CustomUser)
# def save_profile(sender, instance, **kwargs):
#     instance.profile.save()