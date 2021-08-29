from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


from django.dispatch import receiver
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    short_intro = models.CharField(max_length=100 ,blank=True, null=True)
    bio_content = models.TextField(blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    date_joined = models.DateTimeField(default=timezone.now)
    profile_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


# @receiver(post_save,sender=Profile)
# def save_profile(sender,instance,**kwargs):
#     instance.profile.save()