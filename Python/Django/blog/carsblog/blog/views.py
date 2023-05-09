from django.shortcuts import render, get_object_or_404
from .models import BlogPost

# Create your views here.

def home(req):
    posts = BlogPost.objects.all()
    return render(req, 'index.html', {'posts': posts})

def detail(req, postId):
    post = get_object_or_404(BlogPost, pk=postId)
    return render(req, 'detail.html', {'post':post})