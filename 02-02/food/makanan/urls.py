from django.urls import path

from . import views

urlpatterns = [
    path('', views.readMakanan, name='readMakanan'),
    path('minuman/', views.readMinuman, name='readMinuman'),  
    path('pesanan/', views.readPesanan, name='readPesanan'),
    path('hapus/<id>', views.hapus),
]