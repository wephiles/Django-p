# Generated by Django 4.2.1 on 2023-05-06 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app01", "0003_remove_userinfo_password"),
    ]

    operations = [
        migrations.AddField(
            model_name="userinfo",
            name="password",
            field=models.CharField(default=10, max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="userinfo",
            name="size",
            field=models.IntegerField(default=2),
        ),
    ]
