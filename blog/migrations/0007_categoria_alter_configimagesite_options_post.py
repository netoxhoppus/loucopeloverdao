# Generated by Django 5.0.4 on 2024-04-19 02:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_rename_configsite_configimagesite_delete_meumodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.AlterModelOptions(
            name='configimagesite',
            options={'verbose_name_plural': 'Configurações do site'},
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(default='', max_length=70)),
                ('posted_on', models.DateTimeField(auto_now=True)),
                ('corpo', models.TextField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.categoria')),
            ],
        ),
    ]
