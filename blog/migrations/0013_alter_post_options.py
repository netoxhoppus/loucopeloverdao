# Generated by Django 5.0.4 on 2024-04-22 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0012_alter_post_corpo"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="post",
            options={"verbose_name": "Post", "verbose_name_plural": "Posts"},
        ),
    ]
