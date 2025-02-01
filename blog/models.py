from django.db import models
from tinymce.models import HTMLField
#Thumbnail
from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image
import os
from io import BytesIO
from django.core.files.base import ContentFile
from django.template.defaultfilters import slugify
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
    thumbnail = models.ImageField(upload_to="blog/img/post/thumbnails", blank=True)
    def save(self, *args, **kwargs):
        if self.imagem:
            self.create_thumbnail()
        super(Post, self).save(*args, **kwargs)
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
    def __str__(self):
        return self.titulo
    def create_thumbnail(self):
        image = Image.open(self.imagem)
        image.thumbnail((200, 200))  # Tamanho da miniatura (ajuste conforme necessário)
        thumbnail_io = BytesIO()
        image.save(thumbnail_io, 'JPEG', quality=85)  # Pode ajustar o formato e a qualidade conforme necessário
        thumbnail_name = f"thumbnail_{slugify(self.titulo)}.jpg"  # Nome da miniatura
        self.thumbnail.save(thumbnail_name, ContentFile(thumbnail_io.getvalue()), save=False)
class Categoria(models.Model):
    nome = models.CharField(max_length=20, blank=False, default="")
    def __str__(self):
        return self.nome
