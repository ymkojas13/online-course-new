from django.db import models

# Create your models here
# ['Firstname','Lastname','Email','Contact','Address','Gender','Password','Confirm_password','Software_courses']
class online(models.Model):
    Firstname = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Contact= models.IntegerField()
    Address=models.CharField(max_length=50)
    Gender=models.CharField(max_length=50)
    Password=models.CharField(max_length=50)
    Confirm_password=models.CharField(max_length=50)
    Software_courses=models.CharField(max_length=50)

