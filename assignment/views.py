from django.shortcuts import render, get_object_or_404, redirect
from .models import Assignment
from .forms import AssignmentEditForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required 
def assignmentview(request):
	assignments = Assignment.objects.filter(user=request.user)
	return render(request, 'assignment/assignmentview.html', {'assignments':assignments})

@login_required 
def assignmentadd(request):
    if request.method == 'GET':
        return render(request, 'assignment/assignmentadd.html', {'form':AssignmentEditForm()})
    else:
        try:
            form = AssignmentEditForm(request.POST)
            newassignment = form.save(commit=False)
            newassignment.user = request.user
            newassignment.save()
            return redirect('assignmentview')
        except ValueError:
            return render(request, 'assignment/assignmentadd.html', {'form':AssignmentEditForm(), 'error':'Entered wrong data!'})

@login_required
def assignmentedit(request, pk):
    edit = get_object_or_404(Assignment, pk=pk, user=request.user)
    if request.method == 'GET':
        edit_forms = AssignmentEditForm(instance=edit)
        return render(request, 'assignment/assignmentedit.html', {'edit':edit, 'edit_forms':edit_forms})
    else:
        try:
            edit_forms = AssignmentEditForm(request.POST, instance=edit)
            edit_forms.save()
            return redirect('assignmentview')
        except ValueError:
            return render(request, 'assignment/assignmentedit.html', {'edit':edit, 'edit_forms':edit_forms, 'error':'Bad Info'})