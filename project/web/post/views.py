from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.views import View
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
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

def PostDetail(request, Id):
  post = models.Post.objects.get(pk = Id)
  return render(request, 'post-detail.html', {'post':post})

@method_decorator(csrf_exempt, name="post")
@method_decorator(csrf_exempt, name="delete")
class PostLike(View):
  def get(self, request, postId):
    LikeJSON = []
    likeList = models.PostLike.objects.filter(post__pk = postId)
    for like in likeList:
      LikeJSON.append(model_to_dict(like))
      likeList = json.dumps(LikeJSON)
    return JsonResponse(likeList, safe=False)

  def post(self, request, postId):
    newlike = models.PostLike(post__pk = postId, user = request.user)
    newlike.save()
    return JsonResponse({'error':0})
  
  def delete(self, request, postId):
    try:
      like = models.PostLike.objects.get(post__pk = postId, user = request.user)
      like.delete()
      return JsonResponse({'error':0})
    except Exception as e:
      print(e)
      return JsonResponse({'error':1})
  # 돌면서 post_id에 얼마나 많은 user_id의 수가 매칭되었는지 저장을 해야되는데.. 그래서.. 