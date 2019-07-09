from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detalhesFonte.html', views.detalhesFonte, name='detalhesFonte'),
]