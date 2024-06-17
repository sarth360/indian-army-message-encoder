from django.urls import path
from .views import encode_view

urlpatterns = [
    path('encode/', encode_view, name='encode'),
]
