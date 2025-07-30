from django.db import models
from homepage.models import userinfo

# Create your models here.

class Expense(models.Model):
    user = models.ForeignKey(userinfo,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100) 
    date = models.DateTimeField(auto_now_add=True)
    

    
    def __str__(self):
        return f"{self.user.name} - {self.title} - {self.cost}"


    


