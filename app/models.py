from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    location = models.CharField(max_length=100, blank=True)
    birthdate = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['user']
        db_table = user_profiles

    def __str__(self):
        return self.user.username

