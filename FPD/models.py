from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
import random
from datetime import datetime
import os


def upload_image_path(instance, filename):
    now = datetime.now() #
    randint=random.randint(1,99999999)
    name, ext = os.path.splitext(os.path.basename(filename))
    return "pest_images/{year}/{month}/{day}/{randint}{ext}".format(randint=randint, ext=ext, year=now.strftime("%Y"),
                                                                    month=now.strftime("%m"), day=now.strftime("%d"))


class UserProfileManager(BaseUserManager):
    '''
    Manager for user profiles'''

    def create_user(self, email, name, password=None):
        '''create a new user profile'''


        if not email:
            raise ValueError("User must have an email address")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        '''creating and saving a new superuser'''


        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user


class Farmer(AbstractBaseUser, PermissionsMixin):
    '''Database model for users in the system'''

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    phoneNo = models.IntegerField(max_length=255, unique=True)


    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        '''Retrieve full name of user'''

        return self.name

    def get_short_name(self):
        '''Retrieve short name'''

        return self.name

    def __str__(self):
        '''return str representation of user'''

        return self.email


class Pest(models.Model):
    '''Database model for users in the system'''

    name = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    behaviour = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    habitat = models.CharField(max_length=255)


class Crop(models.Model):
    '''Database model for users in the system'''

    description = models.CharField(max_length=255)
    threat = models.ManyToManyField(Pest)
    species = models.CharField(max_length=255)
    commonName = models.CharField(max_length=255)
    family = models.CharField(max_length=255)


class Farm(models.Model):
    '''Database model for farms in the system'''

    owner = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)


class Solution(models.Model):
    '''Database model for farms in the system'''

    solution = models.CharField(max_length=255)


class ControlMeasure(models.Model):
    '''Database model for farms in the system'''

    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    pest = models.ForeignKey(Pest, on_delete=models.CASCADE)
    solutions = models.ForeignKey(Solution, on_delete=models.CASCADE)


class History(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    pest = models.ForeignKey(Pest, on_delete=models.CASCADE)
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    accuracy = models.DecimalField(decimal_places=4)
    pestImage = models.ImageField(upload_to=upload_image_path)







