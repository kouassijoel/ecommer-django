from django.db import models
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    Phone_number = models.CharField(max_length=50)
    date_joined_for_format = models.DateTimeField(auto_now_add=True)
    last_login_for_format  = models.DateTimeField(auto_now_add=True)
    def date_joined(self):
        return self.date_joined_for_format.strftime('%B %d %Y')
    def last_login(self):
        return self.last_login_for_format.strftime('%B %d %Y')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']


    def __str__(self):
        return self.email
    
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class UserProfile(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    address = models.TextField(blank=True, max_length=500)
    profile_picture = models.ImageField(blank=True, upload_to='userprofile',default='static/user_image_default.png')
    city = models.CharField(blank=True, max_length=20)
    state = models.CharField(blank=True, max_length=20)
    country = models.CharField(blank=True, max_length=20)

    def __str__(self):
        return self.user.first_name
