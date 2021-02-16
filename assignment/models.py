from django.db import models
from django.contrib.auth.models import User


class UnitList(models.Model):
    unit = models.CharField(max_length=100)
    unitname = models.CharField(max_length=100)
    unitdescription = models.CharField(max_length=200)
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.unit

class Assignment(models.Model):
    afsn = models.CharField(max_length=100, blank=True)
    unit = models.ForeignKey(UnitList, on_delete=models.CASCADE)
    sub_unit = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    office = models.CharField(max_length=100)
    startdate = models.DateField(null=True, blank=True)
    enddate = models.DateField(null=True, blank=True)
    category_choice = (
        ("Primary", "Primary Duty"),
        ("Additional", "Additional Duty"),
    )
    category = models.CharField(choices=category_choice, max_length=20, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
   
    def __str__(self):
        return self.afsn
