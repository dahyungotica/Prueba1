from django.contrib import admin
from django.urls import path
from PaginaTwice.vista import index
from PaginaTwice.vista import login
from PaginaTwice.vista import informacion
from PaginaTwice.vista import discography
from PaginaTwice.vista import galery
from PaginaTwice.vista import fanArts
from PaginaTwice.vista import productos
from . import vista

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login),
    path('login/index.html/', index),
    path('login/index.html/informacion.html/', informacion),
    path('login/index.html/discography.html/', discography),
    path('login/index.html/galery.html/', galery),
    path('login/index.html/fanArts.html/', fanArts),
    path('login/index.html/productos.html/', productos),
]
