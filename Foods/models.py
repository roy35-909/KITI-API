from django.db import models

# Create your models here.


class Foods(models.Model):

    name = models.CharField(max_length = 255, null=True, blank=True)
    price = models.IntegerField(null=True,blank=True)
    description = models.TextField(max_length = 500,null=True,blank=True)
    photo = models.ImageField(upload_to='Foods/')

    def __str__(self) -> str:
        return self.name 
    

    