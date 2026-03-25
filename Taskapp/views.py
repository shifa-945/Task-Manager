from django.shortcuts import redirect, render

from Taskapp.forms import TaskForm,UserRegistrationForm
from Taskapp.models import Task
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required



# Create your views here.

def home(request):
    return render(request,'home.html')

def register(request):
    if request.method=='POST':
        form=UserRegistrationForm(request.POST)
        form.is_valid()
        user=form.save()
        login(request,user)
        return redirect('home')
    else:
        form=UserRegistrationForm()

    return render(request,'register.html',{'form':form})

def User_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('after_login')
    return render(request,'login.html')

def after_login(request):
    return render(request,'after_login.html')

def User_logout(request):
     logout(request)
     return redirect('home')     
        
@login_required
def Task_add(request):
    if request.method=='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') 
    else:
        form = TaskForm()
       
    return render(request,'Task_add.html', {'form': form})


@login_required
def Task_list(request):
    tasks=Task.objects.all()
    return render(request,'Task_list.html',{'tasks': tasks})

def toggle_task(request,id):
    task=Task.objects.get(id=id)
    task.is_completed=not task.is_completed
    task.save()
    return redirect('Task_list')

@login_required
def Task_delete(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('Task_list')