from django.shortcuts import render, redirect ,get_object_or_404
from django.contrib.auth.models import User 
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from .models import *
from rest_framework.views import APIView
from django.http import JsonResponse
from .forms import UserForm
from django.contrib.auth.decorators import login_required
from .forms import UploadFileForm
from django.shortcuts import render
from .forms import QueryBuilderForm


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('upload_data') 
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})

def upload_data(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'File Uploaded Successfully!')
            return redirect('upload_data')   
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def success(request):
    return render(request, 'success.html')



def query_builder(request):
    if request.method == 'POST':
        form = QueryBuilderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('query_builder')  
    else:
        form = QueryBuilderForm()
    return render(request, 'query.html', {'form': form})

def query_success(request):
    return render(request, 'query.html')


def users(request):
    all_users = User.objects.all()
    return render(request, 'users.html', {'users': all_users})

def logout_view(request):
    return redirect('login')  

def users(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'User added successfully.')
            return redirect('users')
    else:
        form = UserForm()
    all_users = User.objects.all()
    return render(request, 'users.html', {'users': all_users, 'form': form})

def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New user added')
            return redirect('users')  
    else:
        form = UserForm()
    return render(request, 'add_user.html', {'form': form})

@login_required
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return redirect('users')
