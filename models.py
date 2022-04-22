from django.db import models

# Create your models here.

class InfoModel(models.Model):
    fname = models.CharField(max_length = 20)
    lname = models.CharField(max_length = 20)
    email = models.EmailField(max_length = 100)
    phone = models.IntegerField(blank = True, null = True)
    
    def __str__(self):
        return f'{self.fname} {self.lname}  {self.email} {self.phone}'