from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import allthreads

User = get_user_model()

# Create your views here.
def home(request):
    if request.method == 'POST':
        category = request.POST['category']
        product = request.POST['product']
        topic = request.POST['topic']
        content = request.POST['content']
        print(category,product,topic,content)
        b = allthreads(category=category,product=product,topic=topic,content=content,user=request.user)
        b.save()
        return redirect('dash')
    all_entries = allthreads.objects.all().order_by('-dateandtime')
    return render(request,'forum/index.html',{'all_entries':all_entries})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('dash')
        else:
            return redirect('login')
    else:
        return render(request, 'forum/login_user.html',{})

def logout_user(request):
    logout(request)
    return redirect('login')

def signup_user(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        mobile = request.POST['mobile']
        username = first_name
        user = User.objects.create_user(username=first_name,email=email,password=password,first_name=first_name,last_name=last_name,mobile=mobile)
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('dash')
        else:
            return redirect('dash')
    else:
        return render(request, 'forum/signup_user.html',{})

def user_account(request):
    personal_entries = allthreads.objects.filter(user=request.user).order_by('-dateandtime')
    return render(request, 'forum/user-account.html',{'personal_entries':personal_entries})

def user_thread_comments(request):
    return render(request, 'forum/user-thread-comments.html',{})
