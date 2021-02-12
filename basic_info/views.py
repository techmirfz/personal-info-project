from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import BasicInfo
from .forms import BasicInfoForm
from django.db import IntegrityError
from django.contrib.auth.models import User

def home(request):
	return render(request, 'basic_info/home.html')

def signupuser(request):
	if request.method == 'GET':
		return render(request, 'basic_info/signupuser.html', {'form':UserCreationForm()})
	else:
		if request.POST['password1'] == request.POST['password2']:
			try:
				user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
				user.save()
				login(request, user)
				return redirect('home')
			except IntegrityError:
				return render(request, 'basic_info/signupuser.html', {'form': UserCreationForm(), 'error':'Username already exists!'})
		else:
			return render(request, 'basic_info/signupuser.html', {'form': UserCreationForm(),'error':'Password did not match!'})

def loginuser(request):
	if request.method == 'GET':
		return render(request, 'basic_info/loginuser.html', {'form':AuthenticationForm()})
	else:
		user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
		if user is None:
			return render(request, 'basic_info/loginuser.html', {'form':AuthenticationForm(), 'error':'Username and Password did not match!'})
		else:
			login(request, user)
			return redirect('home')	

@login_required 			
def logoutuser(request):
	if request.method == 'POST':
		logout(request)
		return redirect('home')

@login_required 
def basicinfoview(request):
	basics = BasicInfo.objects.filter(user=request.user)
	return render(request, 'basic_info/basicinfoview.html', {'basics':basics})

@login_required 
def basicinfoadd(request):
    if request.method == 'GET':
        return render(request, 'basic_info/basicinfoadd.html', {'form':BasicInfoForm()})
    else:
        try:
            form = BasicInfoForm(request.POST)
            newtraining = form.save(commit=False)
            newtraining.user = request.user
            newtraining.save()
            return redirect('basicinfoview')
        except ValueError:
            return render(request, 'basic_info/basicinfoadd.html', {'form':BasicInfoForm(), 'error':'Entered wrong data!'})

@login_required 
def basicinfoedit(request):
	basics = get_object_or_404(BasicInfo, user=request.user)
	if request.method == 'GET':
		form = BasicInfoForm(instance=basics)
		return render(request, 'basic_info/basicinfoedit.html', {'basics':basics, 'form':form})
	else:
		try:
			form = BasicInfoForm(request.POST, instance=basics,)
			form.save()
			return redirect('basicinfoview')
		except ValueError:
			return render(request, 'basic_info/basicinfoedit.html', {'basics':basics, 'form':form, 'error':'Bad Info'})