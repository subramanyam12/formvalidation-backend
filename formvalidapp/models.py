from django.db import models

# Create your models here.

class Profile(models.Model):
    firstname=models.CharField(max_length=100,blank=True,null=True)
    lastname=models.CharField(max_length=100,blank=True,null=True)
    email=models.EmailField(blank=True,null=True)
    mobile = models.CharField(max_length=20,blank=True,null=True)
    address=models.TextField(blank=True,null=True)
    country=models.CharField(max_length=100,blank=True,null=True)
    state = models.CharField(max_length=100,blank=True,null=True)
    zipcode= models.CharField(max_length=20,blank=True,null=True)
    
    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    