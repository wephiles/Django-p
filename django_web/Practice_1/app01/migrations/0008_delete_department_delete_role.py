# Generated by Django 4.2.1 on 2023-05-06 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app01", "0007_remove_userinfo_height_remove_userinfo_size_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Department",
        ),
        migrations.DeleteModel(
            name="Role",
        ),
    ]
