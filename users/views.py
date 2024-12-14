from django.shortcuts import render, redirect
from .forms import UserSignupForm , UserLoginForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
#  here we use it to restrict the user from other pages or views
from django.contrib.auth.decorators import login_required
# Create your views here.

def sign_up(request):
    if request.user.is_authenticated:
        return redirect('reports:home')
    else:
        if request.method =='POST':
            form = UserSignupForm(request.POST)
            if form.is_valid():
                form.save()
                # here we get the username of user and show it in flash message
                user = form.cleaned_data.get('username')
                messages.success(request, 'you successfylly sign uped ' + user)
                # login(form.save())
                # user = form.save()
                # login(request.user)
                return redirect('users:login')
        else:
            form = UserSignupForm()
        return render(request, 'users/sign_up.html', {'form':form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('reports:home')
    else:
        if request.method == 'POST':
            form = UserLoginForm(request.POST)
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username = username, password = password)
            if user is not None:
                login(request,user)
                return redirect('reports:home')
            # we show the info or error message
            else:
                messages.info(request, 'Username or Password is incorrect')
        else:
            form = UserLoginForm() 
        return render(request, 'users/login.html',{'form':form})
@login_required(login_url='users:login')
def logout_view(request):
    logout(request)
    return redirect('users:login')
    # return render(request, 'users/logout.html')