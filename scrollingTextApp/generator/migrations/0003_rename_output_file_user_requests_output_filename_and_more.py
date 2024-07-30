# Generated by Django 5.0.7 on 2024-07-24 13:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("generator", "0002_user_requests_delete_requests"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user_requests",
            old_name="output_file",
            new_name="output_filename",
        ),
        migrations.AlterField(
            model_name="user_requests",
            name="duration",
            field=models.IntegerField(
                default=3,
                validators=[django.core.validators.MaxValueValidator(10)],
                verbose_name="Длительность (сек.)",
            ),
        ),
        migrations.AlterField(
            model_name="user_requests",
            name="font_size",
            field=models.IntegerField(default=40, verbose_name="Размер шрифта"),
        ),
        migrations.AlterField(
            model_name="user_requests",
            name="fps",
            field=models.IntegerField(
                default=30,
                validators=[django.core.validators.MaxValueValidator(60)],
                verbose_name="Кадров в секунду",
            ),
        ),
        migrations.AlterField(
            model_name="user_requests",
            name="height",
            field=models.IntegerField(
                default=100,
                validators=[django.core.validators.MaxValueValidator(1080)],
                verbose_name="Высота",
            ),
        ),
        migrations.AlterField(
            model_name="user_requests",
            name="width",
            field=models.IntegerField(
                default=100,
                validators=[django.core.validators.MaxValueValidator(1920)],
                verbose_name="Ширина",
            ),
        ),
    ]