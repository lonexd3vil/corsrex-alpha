from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from .managers import *

class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    username = models.CharField(max_length=80, default="", unique=True)
    email = models.EmailField(unique=True)
    # phone = models.CharField(default="", unique=True, max_length=10, blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    full_name = models.TextField(default="", unique=True)
    user_about = models.TextField(default="")
    user_image = models.ImageField(upload_to="userProfile", blank=True, null=True)
    gender = (('He/Him','he/him'),('She/Her','she/her'))
    gender = models.TextField(choices=gender, default="unspecified")
    is_supreme = models.BooleanField(default=False)
    account_status = (('Active','active'),('Inactive','inactive'))
    account_status = models.CharField(default="Inactive", max_length=30, choices=account_status)
    REQUIRED_FIELDS = ["email","full_name"]

    object = CustomUserManager()

    def __str__(self) -> str:
        return str(f"Username: {self.username}") + " | " + str(f"Status: {self.account_status}") + " | " + str(f"Supreme: {self.is_supreme}")
    
    class Meta:
        verbose_name = "User Profile"

class userGenre(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    created_at  = models.DateTimeField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True, null=True)
    genreName = models.CharField(max_length=299, default="", blank=False)
    genreUser = models.ManyToManyField(CustomUser, blank=True, related_name='userChoices')

    def __str__(self) -> str:
        return str(self.genreName) + ' - ' + str(self.genreUser.count())
    
    class Meta:
        verbose_name = "User Genre"

class osInformation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    created_at  = models.DateTimeField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True, null=True)
    field_name = models.TextField(default="", blank=True)
    field_data = models.TextField(default="", blank=True)
    user = models.ManyToManyField(CustomUser, blank=False, related_name="userInformation")

    def __str__(self) -> str:
        return str(self.field_name) + " - " + str(self.field_data)

    class Meta:
        verbose_name = "Additional OS Information"