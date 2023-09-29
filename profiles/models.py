from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


class UserAccount(models.Model):
    '''A user account for holding previouse 
    delivery info 
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_street_address1 = models.CharField(max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(max_length=80, null=True, blank=True)
    default_county = models.CharField(max_length=25, null=True, blank=True)
    default_postcode = models.CharField(max_length=10, null=True, blank=True)
    default_phone_number = models.CharField(max_length=15, null=True, blank=True)
    default_email = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user(sender, instance, created, **kwargs):
    if created:
        UserAccount.objects.create(user=instance)
    instance.useraccount.save()
