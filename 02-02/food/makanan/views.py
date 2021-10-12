from django.db import models
from django.shortcuts import render, redirect
from . import models
# Create your views here.

def readMakanan(req):
    if req.POST:
        input_jenis = req.POST["jenis"]
        input_nama = req.POST["nama"]
        input_harga = req.POST["harga"]
        models.makanan.objects.create(jenis = input_jenis, nama= input_nama, harga = input_harga)
    data = models.makanan.objects.all()
    return render(req, "makanan/index.html", {
        "data": data,
    })

def hapus(request, id): 
    models.makanan.objects.filter(id = id).delete()
    return redirect('/')

def readMinuman(request):
    if request.POST:
        input_jenis = request.POST["jenis"]
        input_nama = request.POST["nama"]
        input_harga = request.POST["harga"]
        models.minuman.objects.create(jenis = input_jenis, nama = input_nama, harga = input_harga)
    data = models.minuman.objects.all()
    return render(request,"minuman/index.html", {
        "data": data,
    })

def readPesanan(request):
    if request.POST:
        get_makanan = request.POST["makanan"] 
        get_makanan = request.POST["minuman"] 
        get_jumlah_makanan = request.POST["makanan"]
        get_jumlah_minuman = request.POST["makanan"]

        input_makanan = models.makanan.objects.filter(id=get_makanan). first()
        input_makanan = models.minuman.objects.filter(id=get_minuman). first()
        models.pesanan.objects.create(makanan=input_makanan, minuman=input_minuman, jumlah_makanan=get)
    dataMakanan = models.makanan.objects.all()
    dataMinuman = models.minuman.objects.all()
    data = models.pesanan.objects.all()
    return render(request, "pesanan/index.html", {
        "dataMakanan": dataMakanan,
        "dataMinuman": dataMinuman,
        "data": data,

    })
    
