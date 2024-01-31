from django.db import models
# Create your models here.

class userdata(models.Model):  
    name = models.CharField("Enter first name", max_length=50)    
    email     = models.EmailField("Enter Email",max_length=40)  
    password=models.CharField("Enter password",max_length=80)


class filedata(models.Model):    
    r_email     = models.EmailField("Enter Email")  
    file        = models.FileField() # for creating file input 
    key         = models.CharField("Enter key",max_length=80,default='0000000') 
  
    class Meta:  
        db_table = "student"
