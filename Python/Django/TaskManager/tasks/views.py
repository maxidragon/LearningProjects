from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from verify_email.email_handler import send_verification_email

from .forms import TaskForm, UserForm
from .models import Task


def home(req):
    return render(req, 'index.html')


@login_required
def tasks(req):
    myTasks = Task.objects.filter(user=req.user, completeDate__isnull=True)
    completedTasks = Task.objects.filter(user=req.user, completeDate__isnull=False)

    return render(req, 'tasks.html', {'tasks': myTasks, 'completedTasks': completedTasks})


@login_required
def detail(req, taskId):
    task = get_object_or_404(Task, pk=taskId, user=req.user)
    if req.method == 'GET':
        form = TaskForm(instance=task)
        return render(req, 'detail.html', {'task': task})
    else:
        form = TaskForm(req.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks')
        else:
            error = "Something is wrong. Try again!"
            return render(req, 'detail.html', {'task': task, 'error': error})


@login_required
def complete(req, taskId):
    task = get_object_or_404(Task, pk=taskId, user=req.user)
    if req.method == 'POST':
        task.completeDate = timezone.now()
        task.save()
        return redirect('tasks')


@login_required
def delete(req, taskId):
    task = get_object_or_404(Task, pk=taskId, user=req.user)
    if req.method == 'POST':
        task.delete()
        return redirect('tasks')


@login_required
def create(req):
    if req.method == 'GET':
        return render(req, 'create.html')
    else:
        form = TaskForm(req.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = req.user
            task.save()
            return redirect('tasks')
        else:
            error = "Something is wrong. Try again!"
            return render(req, 'create.html', {'error': error})


def signup(req):
    if req.method == 'GET':
        return render(req, 'signup.html', {'form': UserForm()})
    else:
        if req.POST.get('password1') == req.POST.get('password2'):
            form = UserForm(req.POST)
            if form.is_valid():
                 inactive_user = send_verification_email(req, form)
            return redirect('home')
            # try:
            #     user = User.objects.create_user(req.POST.get('username'), "", req.POST.get('password1'))
            # except IntegrityError:
            #     return render(req, 'signup.html', {'message': f"{req.POST.get('username')} is alread taken"})
            # else:
            #     user.save()
        else:
            return render(req, 'signup.html', {'message': 'Password does not match'})


def login_user(req):
    if req.method == 'GET':
        return render(req, 'login.html')
    else:
        username = req.POST.get('username')
        password = req.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(req, user)
            return redirect('home')
        else:
            user = User.objects.filter(username=username).first()
            if user.is_active == False:
                error = 'Please verify your email'
            else:
                error = 'Username or password is incorrect'
            return render(req, 'login.html', {'error': error})


@login_required
def logout_user(req):
    logout(req)
    return redirect('home')
