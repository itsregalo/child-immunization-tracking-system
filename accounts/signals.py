from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, Parent, Doctor, Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        if instance.is_parent:
            Parent.objects.create(user=instance)
        if instance.is_doctor:
            Doctor.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
    if instance.is_parent:
        instance.parent.save()
    if instance.is_doctor:
        instance.doctor.save()  



@receiver(post_save, sender=User)
def create_parent(sender, instance, created, **kwargs):
    if created:
        if instance.is_parent:
            Parent.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_parent(sender, instance, **kwargs):
    if instance.is_parent:
        instance.parent.save()

@receiver(post_save, sender=User)
def create_doctor(sender, instance, created, **kwargs):
    if created:
        if instance.is_doctor:
            Doctor.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    if instance.is_doctor:
        instance.doctor.save()