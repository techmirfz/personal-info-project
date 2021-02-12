from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    coursename = models.CharField(max_length=100)
    coursedescription = models.CharField(max_length=200)
    coursecategory = models.CharField(max_length=50)
    coursefield = models.CharField(max_length=50)

    def __str__(self):
        return self.coursename

class School(models.Model):
    schoolname = models.CharField(max_length=100)
    schoolfullname = models.CharField(max_length=200)
    schooladdress = models.CharField(max_length=50)

    def __str__(self):
        return self.schoolname

class Training(models.Model):
	afsn = models.CharField(max_length=100, blank=True)
	course = models.ForeignKey(Course, on_delete=models.CASCADE)
	school = models.ForeignKey(School, on_delete=models.CASCADE)
	startdate = models.DateField(null=True, blank=True)
	enddate = models.DateField(null=True, blank=True)
	averagegrade = models.CharField(max_length=50, blank=True)
	ranking = models.CharField(max_length=20, blank=True)
	numberofstudents = models.CharField(max_length=20, blank=True)
	completed_choice = (
        ("True", "True"),
        ("False", "False"),
    )
	completed = models.CharField(choices=completed_choice, max_length=20, blank=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.afsn