from django.shortcuts import render, redirect
from . import models

# Create your views here.
def index(request):
    if request.POST:
        input = request.POST["nama"]
        models.tugas.objects.create(nama=input)
        print(input)

    data = models.tugas.objects.all()POST
    return render(request, "index.html.", {
        "datahtml": data,
    })


def hapus(request, id):
    models.tugas.objects.filter(id = id).delete()
    return redirect('/')
    
def detail (request, id):
    data = models.tugas.objects.filter(id=id).first()
    print(data)
    return render(request, "detail.html", {
        "detailData": data,
    })
def edit(request, id):
    if request.POST:
         input = request.POST["nama"]
         print(input)
         models.tugas.objects.filter(id = id).update(nama = input)
         return redirect('/')

    data = models.tugas.objects.filter(id = id).first()
    return render(request, "edit.html", {
    "detailData": data,
    })
