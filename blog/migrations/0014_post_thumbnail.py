# Generated by Django 5.0.4 on 2024-04-22 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0013_alter_post_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="thumbnail",
            field=models.ImageField(blank=True, upload_to="blog/img/post/thumbnails"),
        ),
    ]