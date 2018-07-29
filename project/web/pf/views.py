from django.shortcuts import render
from . import models

def ShowList(request):
    Lists = models.Portfolio.objects.all()
    return render(request, 'list.html', {'Lists' : Lists})

def Detail(request, pk):
    Product = models.Portfolio.objects.get(pk = pk)
    VideoAddress = models.Portfolio.objects.get(pk = pk).video[-1:-12:-1][::-1]
    return render(request, 'product.html', {'Product' : Product, 'Videoaddress' : VideoAddress})
# Create your views here.
# {{ Product.video }}[-1:-12:-1][::-1] 파씽해서 넘겨줄수 있는 방법은 없나?