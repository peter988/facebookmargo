# Generated by Django 4.1.1 on 2023-02-24 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("signuplogin", "0005_posts_users_delete_mypost_delete_mystory_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="number",
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
                ("no", models.IntegerField()),
            ],
        ),
    ]