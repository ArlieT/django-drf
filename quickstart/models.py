from django.db import models

# Create your models here.
class Test(models.Model):
    email = models.EmailField()
    content = models.CharField(max_length=200,null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True) 
    
    
# class Person(models.Model):
    # first_name = models.CharField(max_length=50)
    # last_name = models.CharField(max_length=50)