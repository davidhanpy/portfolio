from django.shortcuts import render
from . import models

# Create your views here.
def ShowList(request):
  PList = models.Porfolio.objects.all()
  return render(request, 'list.html', { 'pList' : PList })

def ShowDetail(request, pk):
  Portfolio = models.Porfolio.objects.get(pk = pk)
  return render(request, 'detail.html', {'Portfolio':Portfolio})