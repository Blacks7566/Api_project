from django.contrib.auth.models import AbstractUser
from django.db import models
from account.managers import UserManager
from django.utils.translation import gettext as _


GENDER = (
    ("Male",'Male'),
    ("Female",'Female'),
    ("Other",'Other'),
)

class User(AbstractUser):
    username = None 
    name = models.CharField(max_length=25)
    email = models.EmailField(_('email address'),unique=True)
    phone = models.CharField(max_length=10,unique=True)
    gender = models.CharField(choices=GENDER,max_length=10)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','phone','gender']
    objects = UserManager()

    def __str__(self):
        return self.email






