from django.db import models

from authentication.models import User

# Create your models here.


class Foods(models.Model):

    name = models.CharField(max_length = 255, null=True, blank=True)
    price = models.IntegerField(null=True,blank=True)
    description = models.TextField(max_length = 500,null=True,blank=True)
    photo = models.ImageField(upload_to='Foods/')

    def __str__(self) -> str:
        return self.name 
    



class Order(models.Model):

    user = models.ForeignKey(User,on_delete = models.CASCADE)

    food = models.ForeignKey(Foods, on_delete = models.CASCADE)

    quantity = models.IntegerField(default = 1)
    
    status = models.CharField(max_length = 50, default = "PENDING")
    def __str__(self) -> str:
        return f'{self.user.first_name} == > {self.food.name}'
    
    