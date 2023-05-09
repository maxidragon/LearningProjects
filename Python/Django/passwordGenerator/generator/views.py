from django.shortcuts import render
from random import choice
import string

from django.utils.datastructures import MultiValueDictKeyError


def home(req):
    return render(req, "home.html")


def password(req):
    length = req.POST['length']
    isNumbers = False
    isSpecials = True
    try:
        numbersPOST = req.POST['numbers']
        if numbersPOST == 'on':
            isNumbers = True
    except MultiValueDictKeyError:
        isSpecials = False
    try:
        specialsPOST = req.POST['specials']
        if specialsPOST == 'on':
            isSpecials = True
    except MultiValueDictKeyError:
        isSpecials = False
    numbers = string.digits
    smallletters = string.ascii_lowercase
    bigletters = smallletters.upper()
    specials = string.punctuation
    pool = smallletters + bigletters
    pool += numbers if isNumbers else ''
    pool += specials if isSpecials else ''
    length = int(length)
    result = ''
    for i in range(0, length):
        result += choice(pool)

    return render(req, "password.html", {'result': result})
