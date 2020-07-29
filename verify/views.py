from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import verifyBackground

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from display.models import custID
from display.forms import custIDForm

from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.decorators import login_required
from display import views


# Create your views here.
# The user signup page




@login_required
def signup(request):
    if request.method =="GET":
        background = verifyBackground.objects.all()
        return render(request, 'verify/signup.html', {'backgrounds':background,'form':UserCreationForm()})
    else:
        #Create a new user
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password = request.POST['password1'])
                user.save()
                form = custIDForm(request.POST)
                newuser = form.save(commit=False)
                newuser.save()
                login(request, user)
                return redirect('membershipHome')
            except IntegrityError:
                background = verifyBackground.objects.all()
                return render(request, 'verify/signup.html', {'backgrounds': background, 'form': UserCreationForm(), 'error': '此帳號已經被使用'})
        else:
            # Tell the user that password doesn't match
            background = verifyBackground.objects.all()
            return render(request, 'verify/signup.html', {'backgrounds': background, 'form': UserCreationForm(), 'error':'兩次輸入的密碼不同'})

@login_required
def logoutuser(request):
    if request.method == "POST":
        logout(request)
        return redirect ('home')

# The user login page
def home(request):
    if request.method =="GET":
        background = verifyBackground.objects.all()
        return render(request, 'verify/home.html', {'backgrounds':background,'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            background = verifyBackground.objects.all()
            return render(request, 'verify/home.html', {'backgrounds': background, 'form': AuthenticationForm(), 'error': '帳號密碼錯誤' })
        else:
            login(request, user)
        return redirect('membershipHome')

# To register as administrator
def adminRegister(request):
        if request.method == "GET":
            background = verifyBackground.objects.all()
            return render(request, 'verify/adminRegister.html', {'backgrounds': background, 'form': UserCreationForm()})
        else:
            # Create a new user
            if request.POST['password1'] == request.POST['password2']:
                try:
                    user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                    user.save()
                    form = custIDForm(request.POST)
                    form.isAdmin = 'True'
                    newuser = form.save(commit=False)
                    newuser.save()
                    login(request, user)
                    return redirect('membershipHome')
                except IntegrityError:
                    background = verifyBackground.objects.all()
                    return render(request, 'verify/adminRegister.html',
                                  {'backgrounds': background, 'form': UserCreationForm(), 'error': '此帳號已經被使用'})
            else:
                # Tell the user that password doesn't match
                background = verifyBackground.objects.all()
                return render(request, 'verify/adminRegister.html',
                              {'backgrounds': background, 'form': UserCreationForm(), 'error': '兩次輸入的密碼不同'})
