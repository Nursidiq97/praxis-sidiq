from django.shortcuts import render

# Create your views here.
def readMakanan(request):
    if request.POST:
        input_nama = request.POST["nama"]
        input_jenis = request.POST["jenis"]
        input_harga = request.POST["harga"]

        models.makanan.obcects.create(jenis = input_jenis, nama = input_nama, harga = input_harga)
    data = models.makanan.objects.all()
    return render(req, "makananan/index.html",{
        "data": data,
    })
def readMinuman(request):
    if request.POST:
        input_nama = request.POST["nama"]
        input_jenis = request.POST["jenis"]
        input_harga = request.POST["harga"]

    models.makanan.obcects.create(jenis = input_jenis, nama = input_nama, harga = input_harga)
    data = models.minuman.objects.all()
    return render(req, "minuman/index.html",{
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
    return render(request, "pesanan/index.html",{
        "dataMakanan": dataMakanan,
        "dataMinuman": DataMinuman,
        "data": data,

    })
    