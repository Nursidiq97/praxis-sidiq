from django.urls import path

from . import views

urlpatterns = [ 
    path('', views.readMakanan, name='readMakanan'),
    path('minuman/', views.readMinuman, name='readMinuman'),  
    path('pesanan/', views.readPesanan, name='readPesanan'),
    path('hapus/<id>', views.hapus),
    path('detail/<id>', views.detail),
    path('edit/<id>', views.edit),
    path('detail/<id>', views.detailmakanan),
    path('hapus_minuman/<id>', views.hapusminuman), 
    path('hapus_pesanan/<id>', views.hapuspesanan), 
]