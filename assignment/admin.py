from django.contrib import admin
from .models import Assignment

class AssignmentAdmin(admin.ModelAdmin):
	list_display = ['afsn', 'unit', 'sub_unit', 'designation','office','startdate','enddate','category']
	list_filter = ['afsn', 'unit']
	search_fields = ['afsn', 'unit']

admin.site.register(Assignment, AssignmentAdmin)



