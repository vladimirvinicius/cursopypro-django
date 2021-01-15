from django.urls import path
from pypro.aperitivos.views import video
from pypro.aperitivos.views import indice

app_name = 'aperitivos'
urlpatterns = [
    path('<slug:slug>', video, name='video'),
    path('', indice, name='indice'),
]
