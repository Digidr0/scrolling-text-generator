# Generated by Django 5.0.7 on 2024-07-23 15:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("generator", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="User_requests",
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
                ("text", models.TextField(max_length=255, verbose_name="Текст")),
                (
                    "text_color",
                    models.CharField(max_length=8, verbose_name="Цвет текста"),
                ),
                ("bg_color", models.CharField(max_length=8, verbose_name="Цвет фона")),
                ("font_size", models.IntegerField(default=40)),
                (
                    "output_file",
                    models.TextField(
                        default="video.mov", verbose_name="Название файла"
                    ),
                ),
                (
                    "width",
                    models.IntegerField(
                        default=100,
                        validators=[django.core.validators.MaxValueValidator(1920)],
                    ),
                ),
                (
                    "height",
                    models.IntegerField(
                        default=100,
                        validators=[django.core.validators.MaxValueValidator(1080)],
                    ),
                ),
                (
                    "duration",
                    models.IntegerField(
                        default=3,
                        validators=[django.core.validators.MaxValueValidator(10)],
                    ),
                ),
                (
                    "fps",
                    models.IntegerField(
                        default=30,
                        validators=[django.core.validators.MaxValueValidator(60)],
                    ),
                ),
            ],
            options={
                "verbose_name": "Запросы пользователей на генерацию",
                "verbose_name_plural": "Запросы пользователей на генерацию",
            },
        ),
        migrations.DeleteModel(
            name="Requests",
        ),
    ]
