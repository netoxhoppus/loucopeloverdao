from .models import ConfigImageSite

def conf_imgs(request):
    imgs = ConfigImageSite.objects.all()
    context = {"imgs": imgs}
    return context
