from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.contrib.auth.password_validation import validate_password
import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'


def signup(req):
    if req.method == 'GET':
        return render(req, 'signup.html')
    else:
        if checkEmail(req.POST['email']):
            if not User.objects.filter(email=req.POST['email']).exists():
                if req.POST.get('password1') == req.POST.get('password2'):
                    if not User.objects.filter(username=req.POST['username']).exists():
                        try:
                            validate_password(req.POST.get('password1'))
                        except ValidationError as e:
                            return render(req, 'signup.html', {'messages': e.messages, 'email': req.POST['email'],
                                                               'username': req.POST['username']})
                        else:
                            user = User.objects.create_user(req.POST.get('username'), "", req.POST.get('password1'))
                            user.save()
                            return redirect('forum:home')
                    else:
                        return render(req, 'signup.html', {'message': f"{req.POST.get('username')} is already taken"})
                else:
                    return render(req, 'signup.html', {'message': 'Password does not match'})
            else:
                return render(req, 'signup.html', {'message': 'Email is already taken'})
        else:
            return render(req, 'signup.html', {'message': 'Email is not valid'})


def checkEmail(email):
    if re.fullmatch(regex, email):
        return True
    else:
        return False


def login_user(req):
    if req.method == 'GET':
        return render(req, 'login.html')
    else:
        username = req.POST.get('username')
        password = req.POST.get('password')
        if not User.objects.filter(username=req.POST['username']).exists():
            error = "User does not exist"
            return render(req, 'login.html', {'error': error})
        else:
            user = authenticate(username=username, password=password)
            if user is not None:
                login(req, user)
                return redirect('forum:home')
            else:
                error = 'Password is incorrect'
                return render(req, 'login.html', {'error': error})


@login_required
def logout_user(req):
    logout(req)
    return redirect('forum:home')
