from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from allauth.account.signals import user_logged_in, user_signed_up

# Create your models here.

class profile(models.Model):
    
    name = models.CharField(max_length=120)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(default='description default text')
    
    #location = models.CharField(max_length=120,default='my location default',blank=True,null=True)
    
    #job = models.CharField(max_length=120,default='my location default')


    def __unicode__(self):

        return Self.name

class userStripe(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    stripe_id = models.CharField(max_length=200, null=True, blank=True)

    def __unicode__(self):
        if self.stripe_id:
            return str(self.stripe_id)
        else:
            return self.user.username

def my_callback(sender, request, user, **kwargs):
    print("Request finished!")
    print (user)


user_logged_in.connect(my_callback)
