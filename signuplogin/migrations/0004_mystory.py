# Generated by Django 4.1.1 on 2022-10-21 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("signuplogin", "0003_rename_myposts_mypost"),
    ]

    operations = [
        migrations.CreateModel(
            name="mystory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.TextField()),
                ("photo", models.TextField()),
            ],
        ),
    ]