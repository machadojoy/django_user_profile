from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .task import send_new_user_email
from PIL import Image

class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    location = models.CharField(max_length=100, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    image = models.ImageField(default='user.svg', upload_to='profile_pics')

    class Meta:
        ordering = ['user']
        db_table = 'user_profiles'

    def __str__(self):
        return self.user.username


@receiver(signal=pre_save, sender=User)
def create_username(sender, instance, *args, **kwargs):
    instance.username = instance.first_name[:1] + instance.last_name


@receiver(signal=post_save, sender=User)
def create_or_update_profile(sender, instance, created, **kwargs):
    if created:
        location = getattr(instance, 'location', None)
        birthday = getattr(instance, 'birthday', None)
        image = getattr(instance, 'image', None)
        profile = UserProfile.objects.create(user=instance, location=location, birthdate=birthday, image=image)
        send_new_user_email.delay(instance.email)
    instance.userprofile.save()

