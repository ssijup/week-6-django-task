from django.db import models
 
class userdetails(models.Model):
    #name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    username=models.CharField(unique=True,max_length=100)
    password=models.CharField(max_length=100)


# Create your models here.
