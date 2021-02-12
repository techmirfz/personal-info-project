from django.shortcuts import render, get_object_or_404, redirect
from .models import Assignment
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required 
def assignmentview(request):
	assignments = Assignment.objects.filter(user=request.user)
	return render(request, 'assignment/assignmentview.html', {'assignments':assignments})