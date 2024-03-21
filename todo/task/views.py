from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login as login_user,logout
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from . models import todo
# Create your views here.
def login(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            login_user(request,user)
            messages.info(request,"successfully loggedin")
            return redirect('task')
            # return redirect('studDetails')
        else:
            messages.info(request,"username or password not matched")
            return redirect('login')
    return render(request,'login.html')

def signup(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        confirm_password= request.POST['confirmPassword']
        if confirm_password==password:
            user=User.objects.create_user(username=username,password=password,email=email)
            messages.info(request,'successfully logged in')
            return redirect('login')
        else:
            messages.info(request,"check password and confirm password")
            return redirect("signup")
    return render(request,"signup.html")

@login_required(login_url='login')
def task(request):
    if request.method == "POST":
        task = request.POST.get("task")
        due = request.POST.get("due")
        user=todo.objects.filter(uid_id=request.user.id,task=task, due=due)
        if not user:
            todo.objects.create(task=task,due=due,uid_id=request.user.id)
            messages.info(request,"successfully task added")
            return redirect('display')
        else:
            messages.info(request, "task already exist enter a new task")
            return render(request,'task.html')
    return render(request,'task.html')

def edit(request,id):
    if request.method == 'POST':
        task = request.POST.get("task")
        due = request.POST.get("due")
        todo.objects.filter(id=id).update(task=task,due=due)
        messages.info(request,"successfully updated")
        return redirect("display")
    return render(request,'task.html')

def delete(request,id):
    # if request.method == 'POST':
    #     task = request.POST.get("task")
    #     due = request.POST.get("due")
        todo.objects.filter(id=id).delete()
        messages.info(request,"successfully delete")
        return redirect("display")
    
from django.db.models import Q
def display(request):
    data=todo.objects.filter(Q(status="Not started")|Q(status="In progress"),uid_id=request.user.id)
    #task=todo.objects.filter(uid_id=request.user.id,status="In progress")
    return render(request,"display.html",{'records':data})

def finished(request,id):
    todo.objects.filter(id=id).update(status="completed")
    messages.info(request,'status changed')
    return redirect('display')
def finishedtasks(request):
    tasks = todo.objects.filter(uid_id=request.user.id,status="completed")
    return render(request,'finishedTasks.html',{"tasks":tasks})
def inprogress(request,id):
    todo.objects.filter(id=id).update(status="In progress")
    messages.info(request,'status changed')
    return redirect ('display')

def search(request):
    if request.method=="POST":
        search= request.POST.get('search')
        tasks = todo.objects.filter(uid_id=request.user.id,task=search)
        print(tasks)
        return render(request,'display.html',{"records":tasks})
    return render(request,'display.html')
def due(request):
    if request.method=="POST":
        search= request.POST.get('search')
        tasks = todo.objects.filter(uid_id=request.user.id,due=search)
        print(tasks)
        return render(request,'display.html',{"records":tasks})
    return render(request,'display.html')

def signout(request):
    logout(request)
    messages.info(request,"you are successfully logged out")
    return redirect('home')
def home(request):
    return render(request,'homepage.html')    
    

