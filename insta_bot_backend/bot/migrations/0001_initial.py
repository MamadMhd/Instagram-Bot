# Generated by Django 5.1.3 on 2024-11-20 21:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BotConfig",
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
                ("username", models.CharField(max_length=255)),
                ("password", models.CharField(max_length=255)),
                ("target_hashtags", models.TextField()),
                ("is_active", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="BotLog",
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
                ("action", models.CharField(max_length=255)),
                ("status", models.CharField(max_length=50)),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "bot",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="logs",
                        to="bot.botconfig",
                    ),
                ),
            ],
        ),
    ]