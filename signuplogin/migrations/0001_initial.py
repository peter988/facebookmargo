# Generated by Django 4.1.1 on 2022-09-30 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="myusers",
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
                ("firstname", models.TextField()),
                ("lastname", models.TextField()),
                ("email", models.EmailField(max_length=254)),
                ("password", models.TextField()),
                ("gender", models.TextField()),
            ],
        ),
    ]
