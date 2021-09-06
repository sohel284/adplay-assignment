from django.db import models
from django.contrib.auth.models import User




class UserProfile(models.Model):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    date_of_birth = models.DateField(null=True, blank=True, )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True, blank=True, )
    phone = models.CharField(max_length=20, null=True, blank=True, )
    address = models.TextField(null=True, blank=True, )


    class Meta:
        db_table = 'user_profile'


    def __str__(self):
        return self.phone

    




