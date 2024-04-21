from django.db import models
from tinymce.models import HTMLField

# Create your models here.

class ConfigImageSite(models.Model):
    logo_header = models.ImageField(blank=False, upload_to="configSite/logo")
    header_card = models.ImageField(blank=False, upload_to="configSite/logo")

    class Meta:
        verbose_name_plural = "Configurações do site"
        
    def __str__(self):
        return "Imagens do cabeçalho"


class Post(models.Model):
    categoria = models.ForeignKey("Categoria", on_delete=models.CASCADE)
    titulo = models.CharField(max_length=80, blank=False, default="")
    posted_on = models.DateTimeField(auto_now_add=True)
    edit_on = models.DateTimeField(auto_now=True)
    #corpo = models.TextField(blank=False)
    corpo = HTMLField()
    imagem = models.ImageField(blank=False, upload_to="blog/img/post", default="")

    def __str__(self):
        return self.titulo


class Categoria(models.Model):
    nome = models.CharField(max_length=20, blank=False, default="")
    def __str__(self):
        return self.nome
