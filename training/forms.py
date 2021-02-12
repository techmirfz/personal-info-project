from django import forms
from .models import Training

class TrainingForm(forms.ModelForm):
	class Meta:
		model = Training
		fields = ['afsn', 'course', 'school', 'startdate','enddate','enddate','averagegrade','ranking','numberofstudents','completed']

class TrainingEditForm(forms.ModelForm):
    class Meta:
        model = Training
        fields = ['afsn', 'course','school', 'startdate', 'enddate', 'averagegrade','ranking','numberofstudents','completed']
        
        labels  = {
        'afsn':'AFSN',
        'course':'COURSE',
        'school':'SCHOOL',
        'startdate':'DATE FROM', 
        'enddate':'DATE TO', 
        'averagegrade':'AVERAGE', 
        'ranking':'RANKING', 
        'numberofstudents':'NUMBER OF STUDENTS', 
        'completed':'COMPLETED',  
        }

        widgets = {
            'afsn': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: John Doe'}),
            'course': forms.Select(attrs={'class': 'form-control'}),
            'startdate': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 2018-12-31'}),
            'enddate': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 2018-12-31'}),
            'school': forms.Select(attrs={'class': 'form-control'}),
            'averagegrade': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 30'}),
            'ranking': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 30'}),
            'numberofstudents': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 30'}),
            'completed': forms.Select(attrs={'class': 'form-control'}),
        }

