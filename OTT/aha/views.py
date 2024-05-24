

# Create your views here.
from django.http import FileResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login as login_user,logout
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import path


from . models import Movie,Series

# Create your views here.
# @login_required(login_url='login')
@staff_member_required(redirect_field_name='next', login_url='admin:login')
def upload(request):
    if request.user.is_staff:
        if request.method == "POST":
            name=request.POST.get('name')
            description= request.POST.get('description')
            image= request.FILES.get('image')
            video=request.FILES.get('video')
            cast = request.POST.get('cast')
            Movie.objects.create(name=name,description=description,image=image,video=video,cast=cast)
            messages.info(request,'successfully uploaded')
            return redirect('movies')
        return render(request,'media.html')

# def download(request,id):
#     obj =Movie.objects.get(id=id)
#     filename = obj.name.path
#     response = FileResponse(open(filename,'rb'))
#     return render(request,'download.html',{'response':response})
@staff_member_required(redirect_field_name='next', login_url='admin:login')
def uploadd(request):
    if request.user.is_staff:
        if request.method == "POST":
            name=request.POST.get('name')
            description= request.POST.get('description')
            image= request.FILES.get('image')
            video=request.FILES.get('video')
            cast = request.POST.get('cast')
            Series.objects.create(name=name,description=description,image=image,video=video,cast=cast)
            messages.info(request,'successfully uploaded')
            return redirect('series')
        return render(request,'media.html')




def login(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            login_user(request,user)
            messages.info(request,"successfully loggedin")
            return redirect('movies')
            # return redirect('studDetails')
        else:
            messages.info(request,"username or password not matched")
            return redirect('login')
    return render(request,'login.html')

# login_required(login_url="login")
# def ambajipeta(request):
#     data = Movie.objects.filter(name="ambaji_petamarriage_band")
#     return render (request,"ambajipetamarriageband.html",{"records":data})
@login_required(login_url="login")
def devara(request,id):
    data = Movie.objects.filter(id=id)
    return render (request,"Devara.html",{"records":data})

# def salaar(request):
#     data = Movie.objects.filter(name="ambaji_petamarriage_band")
#     return render (request,"Salaar.html",{"records":data})

# def baby(request):
#     data = Movie.objects.filter(name="Baby")
#     return render (request,"Baby.html",{"records":data})

# def fail_12th(request):
#     data = Movie.objects.filter(name="12thfail")
#     return render (request,"12th_Fail.html",{"records":data})

# def irugapatru(request):
#     data = Movie.objects.filter(name="Irugapatru")
#     return render (request,"Irugapatru.html",{"records":data})

def home(request):
    return render(request,"homepage.html")

# def movies(request):
#     return render(request,'movies.html')

# def ambajipeta(request):
#     data = movies.objects.filter(name="ambaji_petamarriage_band")
#     return render (request,"ambajipetamarriageband.html",{"records":data})

# def ambajipeta(request):
#     data = movies.objects.filter(name="ambaji_petamarriage_band")
#     return render (request,"ambajipetamarriageband.html",{"records":data})

# def ambajipeta(request):
#     data = movies.objects.filter(name="ambaji_petamarriage_band")
#     return render (request,"ambajipetamarriageband.html",{"records":data})

# def ambajipeta(request):
#     data = movies.objects.filter(name="ambaji_petamarriage_band")
#     return render (request,"ambajipetamarriageband.html",{"records":data})



# def signup(request):
#     if request.method=="POST":
#         username = request.POST['name']
#         password = request.POST['age']
#         email = request.POST['email']
#         confirm_password= request.POST['confirm_password']
#         if confirm_password==password:
#             user=User.objects.create_user(username=username,password=password,email=email,confirm_password=confirm_password)
#             messages.info(request,'successfully logged in')
#             return redirect(request,"login.html")
#         else:
#             messages.info(request,"check password and confirm password")
#             return redirect("signup")

def movies(request):
    data = Movie.objects.all()
    print(request.user.is_staff)
    return render (request,"movies.html",{"records":data})

# @login_required(login_url='login')
def signup(request):
    if request.method == "POST":
        username= request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmPassword')
        email = request.POST.get('email')
        if password==confirm_password:
            user=User.objects.create_user(username=username,password=password,email=email,)
            # user.set_password(password)
            # user.save()
            messages.info(request,'successfully registered')
            return redirect('login')
        else:
            messages.info(request,"password does not match")
            return redirect('signup')
    return render(request,'signup.html')

def signout(request):
    logout(request)
    messages.info(request,"you are successfully logged out")
    return redirect('home')

def series(request):
    data = Series.objects.all()
    return render (request,"shows.html",{"records":data})
@login_required(login_url="login")
def display(request,id):
    data = Series.objects.filter(id=id)
    return render(request,'showsDisplay.html',{"records":data})







