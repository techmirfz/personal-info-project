from django.db import models
from django.contrib.auth.models import User

class BasicInfo(models.Model):
	afsn = models.CharField(max_length=10, blank=True, verbose_name='AFSN')
	firstname = models.CharField(max_length=50, blank=True, verbose_name='FIRST NAME')
	middlename = models.CharField(max_length=50, blank=True, verbose_name='MIDDLE NAME')
	lastname = models.CharField(max_length=50, blank=True, verbose_name='LAST NAME')
	extensionname = models.CharField(max_length=50, blank=True, verbose_name='EXTENSION NAME')
	gender_choice = (
        ("Male", "Male"),
        ("Female", "Female"),
    )
	gender = models.CharField(choices=gender_choice, max_length=20, blank=True, verbose_name='GENDER')
	classification_choice = (
        ("Officer", "Officer"),
        ("Enlisted", "Enlisted"),
    )
	classification = models.CharField(choices=classification_choice,max_length=20, blank=True, verbose_name='CLASSIFICATION')
	rank = models.CharField(max_length=20, blank=True, verbose_name='RANK')
	assign = models.CharField(max_length=20, blank=True, verbose_name='CURRENT UNIT')
	source = models.CharField(max_length=20, blank=True, verbose_name='SOURCE OF COMMISION')
	dateentersvc = models.DateField(null=True, blank=True)
	datecompret = models.DateField(null=True, blank=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.afsn


