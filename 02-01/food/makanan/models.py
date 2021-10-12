from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField
# Create your models here.
class makanan(models.Model):
    jenis = models.charlField(max_length=255)   
    nama = charField(max_lenght=255)
    harga = models.interField()

class minuman(models.Model):
    jenis = models.charlField(max_length=255)   
    nama = charField(max_lenght=255)
    harga = models.interField()

class pesanan(models.Model):
    makanan = models.Foreignkey(makanan, on_delete=models.CASCADE)
    jumlah_makanan = models,IntegerField()
    minuman = models.Foreignkey(minuman, on_delete=models.CASCADE)
    jumlah_minuman = models.ItegerField()




