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
        get_minuman = request.POST["minuman"] 
        get_jumlah_makanan = request.POST["jumlah_makanan"]
        get_jumlah_minuman = request.POST["jumlah_minuman"]

        input_makanan = models.makanan.objects.filter(id=get_makanan). first()
        input_minuman = models.minuman.objects.filter(id=get_minuman). first()
        models.pesanan.objects.create(makanan=input_makanan, minuman=input_minuman, jumlah_makanan=get_jumlah_makanan, jumlah_minuman=get_jumlah_minuman)
    dataMakanan = models.makanan.objects.all()
    dataMinuman = models.minuman.objects.all()
    data = models.pesanan.objects.all()
    return render(request, "pesanan/index.html", {
        "dataMakanan": dataMakanan,
        "dataMinuman": dataMinuman,
        "data": data,

    })
def detailpesanan(request, id):
    data = models.pesanan.objects.filter(id=id).first()
    print(data)
    return render(request, "pesanan/detail.html", {
        "detailData": data,
    })

def editpesanan(req, id):
    if req.POST:
        get_makanan = req.POST["makanan"] 
        get_minuman = req.POST["minuman"] 
        get_jumlah_makanan = req.POST["jumlah_makanan"]
        get_jumlah_minuman = req.POST["jumlah_minuman"]

        input_makanan = models.makanan.objects.filter(id=get_makanan). first()
        input_minuman = models.minuman.objects.filter(id=get_minuman). first() 
        models.pesanan.objects.filter(id=id).update(makanan=input_makanan, minuman=input_minuman, jumlah_makanan=get_jumlah_makanan, jumlah_minuman=get_jumlah_minuman)
        return redirect("/pesanan/")
    dataMakanan = models.makanan.objects.all()
    dataMinuman = models.minuman.objects.all() 
    data = models.pesanan.objects.filter(id = id).first()
    return render(req, "pesanan/edit.html", {
        "dataMakanan": dataMakanan,
        "dataMinuman": dataMinuman, 
        "data": data,

    })
  

#Hapus Minuman
def hapusminuman(request, id): 
    models.minuman.objects.filter(id = id).delete()
    return redirect('/')

#Hapus pesanan 
def hapuspesanan(request, id): 
    models.pesanan.objects.filter(id = id).delete()
    return redirect('/')
#Edit & Detail Makanan
def detailmakanan(request, id):
    data = models.makanan.objects.filter(id=id).first()
    print(data)
    return render(request, "makanan/detail.html", {
        "detailData": data,
    })


def editmakanan(request, id):
    if request.POST:
         input = request.POST["nama"]
         print(input)
         models.makanan.objects.filter(id = id).update(nama = input)
         return redirect('/')

    data = models.makanan.objects.filter(id = id).first()
    return render(request, "makanan/edit.html", {
    "detail Data": data,
    })

#Edit & Detail Minuman
def detail(request, id):
    data = models.minuman.objects.filter(id=id).first()
    print(data)
    return render(request, "minuman/detail.html", {
        "detailData": data,
    })

def edit(request, id):
    if request.POST:
         input = request.POST["nama"]
         print(input)
         models.minuman.objects.filter(id = id).update(nama = input)
         return redirect('/')

    data = models.minuman.objects.filter(id = id).first()
    return render(request, "minuman/edit.html", {
    "detailData": data,
    })
    
