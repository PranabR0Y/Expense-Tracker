from django.db import models

# Create your models here.
class userinfo(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Services(models.Model):
    title = models.CharField(max_length=100)
    link = models.URLField(max_length=250,blank=True,null=True)
    image = models.FileField(upload_to='images/',null=True,default=None, max_length=250)
