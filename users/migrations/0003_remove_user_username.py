# Generated by Django 4.1.5 on 2023-02-16 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_user_username"),
    ]

    operations = [
        migrations.RemoveField(model_name="user", name="username",),
    ]