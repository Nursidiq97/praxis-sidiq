from django.shortcuts import render
from . import models

# Create your views here.
def index(request):
    if request.POST:
        input = request.POST["nama"]
        models.tugas.objects.create(nama=input)
        print(input)

    data = models.tugas.objects.all()
    return render(request, "index.html.", {
        "datahtml": data
    })
    



