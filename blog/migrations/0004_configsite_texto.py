# Generated by Django 5.0.4 on 2024-04-18 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_configsite_header_card_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='configsite',
            name='texto',
            field=models.CharField(default='', max_length=20),
        ),
    ]
