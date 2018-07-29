from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.views import View
from django.forms.models import model_to_dict
from . import models

import json

# Create your views here.
def home(request):
  return render(request, 'post-list.html')

# http://brownbears.tistory.com/276
class Post(View):
  def get(self, request):
    postJSON = []
    postList = models.Post.objects.all()

    # postList = serializers.serialize('json', postList)
    for post in postList:
      postJSON.append(model_to_dict(post))
    postList = json.dumps(postJSON)
    return JsonResponse(postList, safe = False)