# Generated by Django 4.2.1 on 2023-05-06 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app01", "0004_userinfo_password_userinfo_size"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userinfo",
            name="age",
            field=models.IntegerField(default=2),
        ),
    ]
