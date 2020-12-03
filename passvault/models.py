from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    pass

class SavedPassword(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="SitePasswords")
    SiteName = models.CharField(max_length=200,blank=False)
    SiteUserName = models.CharField(max_length=200,blank=True,default="No User Name Provide For The Site!")
    PasswordForSite = models.CharField(max_length=300,blank=False,null=False)
    
    def __str__(self):
        return f"Site :{self.SiteName} and username{self.SiteUserName}"
