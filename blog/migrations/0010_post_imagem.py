# Generated by Django 5.0.4 on 2024-04-19 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_post_edit_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='imagem',
            field=models.ImageField(default='', upload_to='blog/img/post'),
        ),
    ]
