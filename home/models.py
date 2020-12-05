from django.db import models

# Create your models here.

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=225)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=100)
    contact = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)
    
# def __str__(self):
#     return 'Message from'self.name + ' - ' + self.email
    

class About(models.Model):
    sno = models.AutoField(primary_key=True)
    author = models.CharField(max_length=225)
    content = models.TextField() 
    # slug = models.CharField(max_length=130)
    # timeStamp = models.DateTimeField(auto_now_add=True, blank=True)
    