from .models import User_requests
from django import forms


class GenerateForm(forms.ModelForm):
    class Meta:
        model = User_requests
        fields = [
            "text",
            "text_color",
            "bg_color",
            # "output_filename",
            "font_size",
            "width",
            "height",
            "duration",
            "fps",
        ]
        widgets = {
            "text": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Текст бегущей строки",
                    "rows": "3",
                }
            ),
            "text_color": forms.TextInput(
                attrs={
                    "class": "form-control mt-1 w-100",
                    "placeholder": "Цвет текста",
                    "id": "text_color",
                    "maxlength": "255",
                    "minlength": "1",
                    "pattern": "^[0-9A-Fa-f]{6}$",
                }
            ),
            "bg_color": forms.TextInput(
                attrs={
                    "class": "form-control mt-1 w-100",
                    "placeholder": "Цвет фона",
                    "id": "bg_color",
                    "maxlength": "255",
                    "minlength": "1",
                    "pattern": "^[0-9A-Fa-f]{6}$",
                }
            ),
            # "output_filename": forms.TextInput(
            #     attrs={
            #         "class": "form-control mt-1 w-100",
            #         "placeholder": "название",
            #         "id": "output_filename",
            #         "maxlength": "255",
            #         "minlength": "1"
            #     }),
            "font_size": forms.NumberInput(
                attrs={
                    "class": "form-control-range m-1 w-100",
                    "placeholder": "Размер шрифта",
                    "id": "font_size",
                    "max": "100",
                    "min": "1",
                }
            ),
            "width": forms.NumberInput(
                attrs={
                    "class": "form-control-range m-1 w-100",
                    "placeholder": "Ширина",
                    "id": "width",
                    "max": "1920",
                    "min": "25",
                }
            ),
            "height": forms.NumberInput(
                attrs={
                    "class": "form-control-range m-1 w-100",
                    "placeholder": "Высота",
                    "id": "height",
                    "max": "1080",
                    "min": "25",
                }
            ),
            "duration": forms.NumberInput(
                attrs={
                    "class": "form-control-range m-1 w-100",
                    "placeholder": "Длительность",
                    "id": "duration",
                    "max": "30",
                    "min": "1",
                }
            ),
            "fps": forms.NumberInput(
                attrs={
                    "class": "form-control-range m-1 w-100",
                    "placeholder": "Кадров/сек",
                    "id": "fps",
                    "max": "60",
                    "min": "1",
                }
            ),
        }
        def clean_text(self):
            text = self.cleaned_data.get('text')
            if text.length < 0:
                raise forms.ValidationError("negative text")
            return text
