from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField

# Create your models here.
class makanan(models.Model):
    jenis = models.CharField(max_length=255)
    nama = CharField(max_length=255)
    harga = models.IntegerField()

class minuman(models.Model):
    jenis = models.CharField(max_length=255)
    nama = CharField(max_length=255)
    harga = models.IntegerField() 

class pesanan(models.Model):
    makanan = models.ForeignKey(makanan, on_delete=models.CASCADE)
    jumlah_makanan = models.IntegerField()
    minuman = models.ForeignKey(minuman, on_delete=models.CASCADE)
    jumlah_minuman = models.IntegerField()


