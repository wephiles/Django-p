# Generated by Django 4.2.1 on 2023-05-06 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app01", "0006_userinfo_height"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userinfo",
            name="height",
        ),
        migrations.RemoveField(
            model_name="userinfo",
            name="size",
        ),
        migrations.AlterField(
            model_name="userinfo",
            name="age",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
