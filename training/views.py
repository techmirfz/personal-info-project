from django.shortcuts import render, get_object_or_404, redirect
from .models import Training
from .forms import TrainingEditForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required 
def trainingview(request):
	trainings = Training.objects.filter(user=request.user)
	return render(request, 'training/trainingview.html', {'trainings':trainings})

@login_required 
def trainingadd(request):
    if request.method == 'GET':
        return render(request, 'training/trainingadd.html', {'form':TrainingEditForm()})
    else:
        try:
            form = TrainingEditForm(request.POST)
            newtraining = form.save(commit=False)
            newtraining.user = request.user
            newtraining.save()
            return redirect('trainingview')
        except ValueError:
            return render(request, 'todo/trainingadd.html', {'form':TrainingEditForm(), 'error':'Entered wrong data!'})

@login_required
def trainingedit(request, pk):
    edit = get_object_or_404(Training, pk=pk, user=request.user)
    if request.method == 'GET':
        edit_forms = TrainingEditForm(instance=edit)
        return render(request, 'training/trainingedit.html', {'edit':edit, 'edit_forms':edit_forms})
    else:
        try:
            edit_forms = TrainingEditForm(request.POST, instance=edit)
            edit_forms.save()
            return redirect('trainingview')
        except ValueError:
            return render(request, 'training/trainingedit.html', {'edit':edit, 'edit_forms':edit_forms, 'error':'Bad Info'})

