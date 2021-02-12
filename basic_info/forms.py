from django import forms
from .models import BasicInfo

class BasicInfoForm(forms.ModelForm):
	class Meta:
		model = BasicInfo
		fields = ['afsn', 'firstname', 'middlename', 'lastname', 'extensionname', 'gender', 'classification', 'rank', 'assign', 'source']


		widgets = {
            'afsn': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'AFSN'}),
            'firstname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'FIRST NAME'}),
            'middlename': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'MIDDLE NAME'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'LAST NAME'}),
            'category': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CATEGORY'}),
            'rank': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'RANK'}),
            'assign': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'UNIT'}),
		   
		    }

