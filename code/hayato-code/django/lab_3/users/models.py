"""
module for authentication models
"""
from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager



class User(AbstractUser):
    """
    custom user model
    """
    username = models.CharField(max_length=255, unique=True)
    first_name = None
    last_name = None
    email = models.EmailField('email address', blank=True, null=True)
    profile_picture = models.ImageField(upload_to="profile_pictures/", blank=True)
   
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.username
    
    @property
    def get_photo_url(self):
        # function to handle situation where the profile picture isn't associated with any file
        if self.profile_picture and hasattr(self.profile_picture, 'url'):
            return self.profile_picture.url
        else:
            return "/static/images/default_user.png"