from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class form(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=254)
    phone_number=models.IntegerField()
    address=models.TextField()

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField(max_length=500, blank=True)
    phone_number = models.CharField(max_length=12, blank=True)
    

    def __str__(self):
        return '%s %s' % (self.user.first_name, self.user.last_name)





@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
