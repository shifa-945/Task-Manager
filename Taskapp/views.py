from django.shortcuts import redirect, render

from Taskapp.forms import TaskForm
from Taskapp.models import Task

# Create your views here.

def home(request):
    return render(request,'home.html')


def Task_add(request):
    if request.method=='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') 
    else:
        form = TaskForm()
       
    return render(request,'Task_add.html', {'form': form})


def Task_list(request):
    tasks=Task.objects.all()
    return render(request,'Task_list.html',{'tasks': tasks})

def toggle_task(request,id):
    task=Task.objects.get(id=id)
    task.is_completed=not task.is_completed
    task.save()
    return redirect('Task_list')

def Task_delete(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('Task_list')