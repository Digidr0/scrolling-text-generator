from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.generate, name='generate'),
    path("user_requests", views.user_requests, name='user_requests'),
    path("output", views.output, name='output'),
    path('http_generate', views.http_generate, name='http_generate'),
]


