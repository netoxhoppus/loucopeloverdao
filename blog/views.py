from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# View para exibir um post específico.
def post(request, id):
    post = Post.objects.filter(pk=id)
    return render(request, "blog/post.html", {"posts": post})

# View para exibir a página inicial.
def home(request):
    post = Post.objects.last()
    return render(request, "blog/home.html", {"last": post})
