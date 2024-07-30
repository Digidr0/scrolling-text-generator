import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import logging
from math import ceil

class FormData:
    def __init__(self, text, text_color, bg_color, font_size, width, height, duration, fps):
        self.text = text
        self.text_color = text_color
        self.bg_color = bg_color
        # self.output_filename = output_filename
        self.font_size = font_size
        self.width = width
        self.height = height
        self.duration = duration
        self.fps = fps

def hex_to_rgb(hex):
    rgb = []
    for i in (0, 2, 4):
        decimal = int(hex.lstrip("#")[i : i + 2], 16)
        rgb.append(decimal)
    return tuple(rgb)


def create_scrolling_text_video(form_data):
    # Определение параметров видео
    output_path = f'./media/output.mp4'
    fourcc = cv2.VideoWriter_fourcc(*'X264')
    # fourcc = cv2.VideoWriter_fourcc(*"XVID")
    # fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    out = cv2.VideoWriter(output_path, fourcc, form_data.fps, (form_data.width, form_data.height))

    # Вычисление общего количества кадров
    total_frames = form_data.duration * form_data.fps

    # Шрифт и начальная позиция текста
    font = ImageFont.truetype("consola.ttf", form_data.font_size)
    text_x = form_data.width  # Начальная позиция текста (за правым краем)
    text_width = font.getlength(form_data.text)

    text_color = hex_to_rgb(form_data.text_color)
    bg_color = hex_to_rgb(form_data.bg_color)

    for frame_num in range(total_frames):
        # Создание пустого изображения

        img = Image.new(
            "RGB", (form_data.width, form_data.height), color=(bg_color[0], bg_color[1], bg_color[2])
        )
        draw = ImageDraw.Draw(img)

        # Рассчет текущей позиции текста
        scroll_speed = ceil((form_data.width + text_width) / total_frames)
        # Скорость прокрутки текста в пикселях на кадр
        text_x -= scroll_speed
        # Рисование текста на изображении
        draw.text(
            (text_x, (form_data.height - form_data.font_size) // 2),
            form_data.text,
            font=font,
            fill=(text_color[0], text_color[1], text_color[2]),
        )

        # Конвертация изображения в формат OpenCV
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        # Запись кадра в видео
        out.write(frame)

    # Освобождение ресурсов
    out.release()
    cv2.destroyAllWindows()