# Generated by Django 5.1.1 on 2024-10-07 12:22

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                (
                    "title",
                    models.CharField(
                        choices=[("Mr", "Mr"), ("Mrs", "Mrs"), ("Ms", "Ms")],
                        default="Mr",
                        max_length=100,
                    ),
                ),
                ("username", models.CharField(max_length=50)),
                ("name", models.CharField(max_length=50)),
                (
                    "email",
                    models.EmailField(default="scaler@scaler.com", max_length=50),
                ),
                (
                    "address",
                    models.CharField(default="Unknown Address", max_length=255),
                ),
            ],
        ),
    ]
