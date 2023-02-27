from django.db import models

# Create your models here.# model = db
# create your databases

#users database
class users(models.Model):
     firstname = models.TextField()
     lastname = models.TextField()
     email = models.TextField()
     password = models.TextField()

#posts database
class posts(models.Model):
     title  = models.TextField()
     mind = models.TextField()
     img = models.TextField()


# number database
class number(models.Model):
     no = models.IntegerField()
     
     
     
 

    