from django.shortcuts import render

from django.http.response import HttpResponse
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

from userprofileapp.models import *
from userprofileapp.forms import *


def sign_up(request):
    form = CreateNewUserForm()
    registered = False
    if request.method == 'POST':
        form = CreateNewUserForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            registered = True
            user_profile = UserProfile(user=user, )
            user_profile.save()
            return redirect('login_page')
    return render(request, 'signup.html', {
        'title': 'Sign Up User', 'form': form,
    })


def login_page(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password, )
            if user is not None:
                login(request, user)
                return redirect('profile')
    return render(request, 'login.html', {'title': 'Login', 'form':form, })


def profile(request, ):
    return render(request, 'user.html', )    


def user_profile_list(request, ):
    users = User.objects.all()
    return render(request, 'user_profile_list.html', {'users': users})

def edit_profile(request):
    current_user = UserProfile.objects.get(user=request.user)
    form = UserProfileForm(instance=current_user, )
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=current_user)
        print(form)
        if form.is_valid():
            form.save(commit=True, )
            form = UserProfileForm(instance=current_user, )
            return redirect('profile')
    return render(request, 'user_profile.html', {'title': 'create Profile. ', 'form':form, })


def delete_profile(request, username):
    user = User.objects.get(username=username)
    user.delete()
    return HttpResponse('User is deleted successfully')

def logout_user(request):
    logout(request)
    return redirect('login_page') 

