from django.contrib import admin
from django import forms
from .models import  ConfigImageSite, Post, Categoria

# Register your models here.
class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'  # Exibir todos os campos, exceto o campo 'thumbnail'
    def __init__(self, *args, **kwargs):
        super(PostAdminForm, self).__init__(*args, **kwargs)
        if 'thumbnail' in self.fields:
            self.fields['thumbnail'].widget.attrs['readonly'] = True  #  o campo 'thumbnail' somente leitura

class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm

admin.site.register(Post, PostAdmin)
admin.site.register(ConfigImageSite)
admin.site.register(Categoria)
