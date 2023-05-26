from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import Taskform
# Create your views here.

def home(request):
    task = Task.objects.all()
    form = Taskform()
    context = {'tasks': task, 'form': form}
    

    if request.method == 'POST':
        task = Task.objects.all()
        form = Taskform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'app/home.html', context)
    

def update(request, id):
    task = Task.objects.get(id=id)
    form = Taskform(instance=task)
    context = {'form': form}

    if request.method == 'POST':
        form = Taskform(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'app/update.html', context)
              

def delete(request, id):
    task = Task.objects.get(id=id)

    if request.method == 'POST':
        task.delete()
        return redirect('/')

    context = {'task': task}
    return render(request, 'app/delete.html', context)
    