from .models import ConfigImageSite, Post

def conf_imgs(request):
    imgs = ConfigImageSite.objects.all()
    return {"imgs": imgs}

def trending_now(request):
    trending_posts = Post.objects.exclude(id=Post.objects.last().id).order_by('-id')[:3]
    return {"trend":trending_posts}
