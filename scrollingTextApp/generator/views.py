from django.shortcuts import render, redirect
from .models import User_requests
from .forms import GenerateForm
from .generate import create_scrolling_text_video, FormData
from django.http import HttpResponse
from .defaults import default_data
import logging
logger = logging.getLogger(__name__)


def generate(request):
    error = ""
    if request.method == "POST":
        print(request.POST)
        form = GenerateForm(request.POST)
        if form.is_valid():
            form_data = {field: form.cleaned_data[field] for field in form.cleaned_data}
            form_data_obj = FormData(**form_data)
            create_scrolling_text_video(form_data_obj)
            form.save()
            return render(request, "generator/output.html")
            # redirect("user_requests")
        else:
            error = "Неверная отправка формы"
    form = GenerateForm()
    context = {"form": form, "error": error}
    return render(request, "generator/generate.html", context)

def http_generate(request):
    if request.method == "GET":

        form_data = {key: request.GET.get(key, default) for key, default in default_data.items()}
        form = GenerateForm(form_data)

        if form.is_valid():
            form_data_obj = FormData(**form.cleaned_data)
            create_scrolling_text_video(form_data_obj)
            form.save()
            logger.info(f"Form data: {form.cleaned_data}")
            return render(request, "generator/output.html")
        else:
            return HttpResponse("Invalid form submission", status=400)
    else:
        return HttpResponse("Invalid request method", status=405)

def user_requests(request):
    requests = User_requests.objects.order_by("-id")
    return render(request, "generator/user_requests.html", {"requests": requests})


def output(request):
    return render(request, "generator/output.html")
