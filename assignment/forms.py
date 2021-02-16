from django import forms
from .models import Assignment

class AssignmentForm(forms.ModelForm):
	class Meta:
		model = Assignment
		fields = ['afsn', 'unit', 'sub_unit', 'designation','office','startdate','enddate','category']

class AssignmentEditForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['afsn', 'unit', 'sub_unit', 'designation','office','startdate','enddate','category']
        
        labels  = {
        'afsn':'AFSN',
        'unit':'COURSE',
        'sub_unit':'SUB-UNIT',
        'designation':'DESIGNATION', 
        'office':'OFFICE', 
        'startdate':'DATE FROM ', 
        'enddate':'DATE TO', 
        'category':'CATEGORYY',  
        }

        widgets = {
            'afsn': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter AFSN'}),
            'unit': forms.Select(attrs={'class': 'form-control'}),
            'sub_unit': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Sub-Unit'}),
            'designation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Designation'}),
            'startdate': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 2018-12-31'}),
            'enddate': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 2018-12-31'}),
            'office': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Office'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }
