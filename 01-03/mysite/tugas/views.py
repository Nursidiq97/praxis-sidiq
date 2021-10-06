from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hallo, Nama Saya Nur Sidiq, Asal Dari Pelembang.")
    return HttpResoonse("Jangan Lupa Bahagia")