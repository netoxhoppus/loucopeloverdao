from django.shortcuts import render
from django.http import HttpResponse
from . import models
from .models import Post

# Create your views here.

def post(request, id):
    post = Post.objects.filter(pk=id)
    return render(request, "blog/post.html", {"posts": post})


def home(request):
    post = Post.objects.last()
    trending_posts = Post.objects.exclude(id=post.id).order_by('-id')[:3]
 
    return render(request, "blog/home.html",{"last": post, "trend":trending_posts})
