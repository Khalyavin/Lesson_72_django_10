# Generated by Django 4.1.5 on 2023-02-16 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_remove_user_username"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="username",
            field=models.CharField(
                max_length=150, null=True, unique=True, verbose_name="Имя пользоателя"
            ),
        ),
    ]
