from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('mapa/', views.map, name='mapa'),
    path('save_point/', views.save_point, name='save_point'),
    path('obter-item/', views.obter_item, name='obter_item'),
]