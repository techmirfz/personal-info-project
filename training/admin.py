from django.contrib import admin
from .models import Training, Course, School


class TrainingAdmin(admin.ModelAdmin):
	list_display = ['afsn', 'course', 'school', 'startdate','enddate','enddate','averagegrade','ranking','numberofstudents','completed']
	list_filter = ['afsn', 'course']
	search_fields = ['afsn', 'course']

admin.site.register(Training, TrainingAdmin)
admin.site.register(Course)
admin.site.register(School)
