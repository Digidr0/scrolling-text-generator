from django.db import models
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
    MinLengthValidator,
    MaxLengthValidator,
)
from .defaults import default_data as dfd

# Create your models here.
class User_requests(models.Model):
    text = models.TextField(
        "Текст",
        max_length=256,
        default=dfd['text'],
        validators=[
            MinLengthValidator(1),  # Minimum length of 4 characters
            MaxLengthValidator(255),  # Maximum length of 150 characters
        ],
        blank=True,
        null=True,
    )
    text_color = models.CharField(
        "Цвет текста", max_length=8, blank=True, null=True, default=dfd['text_color']
    )
    bg_color = models.CharField(
        "Цвет фона", max_length=8, blank=True, null=True, default=dfd['bg_color']
    )

    # output_filename = models.TextField(
    #     "Название файла",
    #     default=dfd['output_filename'],
    #     validators=[
    #         MinLengthValidator(1),  # Minimum length of 4 characters
    #         MaxLengthValidator(255),  # Maximum length of 150 characters
    #     ],blank=True, null=True
    # )
    font_size = models.IntegerField(
        "Размер шрифта", default=dfd['font_size'], validators=[MinValueValidator(1)]
    )
    width = models.IntegerField(
        "Ширина",
        default=dfd['width'],
        validators=[MaxValueValidator(1920), MinValueValidator(25)],
        blank=True,
        null=True,
    )
    height = models.IntegerField(
        "Высота",
        default=dfd['height'],
        validators=[MaxValueValidator(1080), MinValueValidator(25)],
        blank=True,
        null=True,
    )
    duration = models.IntegerField(
        "Длительность (сек.)",
        default=dfd['duration'],
        validators=[MaxValueValidator(30), MinValueValidator(1)],
        blank=True,
        null=True,
    )
    fps = models.IntegerField(
        "Кадров в секунду",
        default=dfd['fps'],
        validators=[MaxValueValidator(60), MinValueValidator(1)],
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Запросы пользователей на генерацию"
        verbose_name_plural = "Запросы пользователей на генерацию"
