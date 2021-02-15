from django import forms
from .models import BasicInfo

class BasicInfoForm(forms.ModelForm):
	class Meta:
		model = BasicInfo
		fields = ['afsn', 'rank', 'firstname', 'middlename', 'lastname', 'extensionname', 'gender', 'classification', 'assign', 'source', 'dateentersvc', 'datecompret']


		widgets = {
            'afsn': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'AFSN'}),
            'rank': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'RANK'}),
            'firstname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'FIRST NAME'}),
            'middlename': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'MIDDLE NAME'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'LAST NAME'}),
            'extensionname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'EXTENSION NAME'}),
            'gender': forms.Select(attrs={'class': 'form-control', 'placeholder': 'GENDER'}),
            'classification': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CLASSIFICATION'}),
            'assign': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CURRENT UNIT'}),
		'source': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'SOURCE OF COMMISSION/ENLISTMENT'}), 
            'dateentersvc': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'DATE ENTERED SERVICE'}),
            'datecompret': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'DATE OF COMPULSORY RETIREMENT'}), 
		}

           
