from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    LIBRARY_ROLES = (
            ('ad', 'Admin'),
            ('li', 'Librarian'),
            ('re', 'Reader'),

        )
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    role = models.CharField(max_length=2, choices=LIBRARY_ROLES, default='re')

    def get_role(self):
        roles_dict = dict(self.LIBRARY_ROLES)
        return roles_dict[self.role]
    
    def get_absolute_url(self):
        return reverse('profile_detail', kwargs={'pk':self.pk})
    
    def __str__(self):
        return self.get_role() +'-'+ self.user.username[0:20]

@receiver(post_save,sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save() 