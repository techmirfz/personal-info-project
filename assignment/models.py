from django.db import models
from django.contrib.auth.models import User

class Assignment(models.Model):
    afsn = models.CharField(max_length=100, blank=True)
    unit = models.CharField(max_length=100)
    sub_unit = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    office = models.CharField(max_length=100)
    startdate = models.DateField(null=True, blank=True)
    enddate = models.DateField(null=True, blank=True)
    category = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
   
    def __str__(self):
        return self.afsn


