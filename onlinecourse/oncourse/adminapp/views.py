from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import Signform
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout


def sign_up(request):
    if request.method == "POST":
        fm = Signform(request.POST)
        if fm.is_valid():
            messages.success(request, 'you have signup successfully')
            fm.save()
    else:
        fm = Signform()
    return render(request, 'signup.html', {'form': fm})


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in successfully')
                    return HttpResponseRedirect('/profile')
        else:
            fm = AuthenticationForm()
        return render(request, 'login.html', {'form': fm})
    else:
        return HttpResponseRedirect('/profile')


def user_profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html', {'name': request.user})
    else:
        return HttpResponseRedirect('/login')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login')


