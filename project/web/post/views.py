from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.views import View
from django.forms.models import model_to_dict
from django.core.paginator import Paginator
from . import models

import json

# Create your views here.
def home(request):
  # postList = models.Post.objects.all()
  # paginator = Paginator(postList, 3)
  
  # page = request.GET.get('page')
  # postList = paginator.get_page(page)
  return render(request, 'post-list.html')#  , {'postList': postList})

# http://brownbears.tistory.com/276
class Post(View):
  def get(self, request):
    postJSON = []
    postList = models.Post.objects.all()
    paginator = Paginator(postList, 3)
    #리스트와 해당 리스트를 한 페이지에 몇개 보여줄 것인가
    page = int(request.GET.get('page', 1))
    postList = paginator.get_page(page)
    # postList = serializers.serialize('json', postList)
    for post in postList:
      postJSON.append(post.to_dict())
    postList = json.dumps({
      'data':postJSON,
      'pageNumber': page,
      'totalPage': paginator.num_pages,
      'totalCount': paginator.count
    })
    return JsonResponse(postList, safe = False)

def PostDetail(request, Id):
  post = models.Post.objects.get(pk = Id)
  return render(request, 'post-detail.html', {'post':post})

class PostLike(View):
  def get(self, request, postId):
    LikeJSON = []
    likeList = models.PostLike.objects.filter(post__pk = postId)
    for like in likeList:
      LikeJSON.append(model_to_dict(like))
      likeList = json.dumps(LikeJSON)
    return JsonResponse(likeList, safe=False)

  def post(self, request, postId):
    post = models.Post.objects.get(pk = postId)
    newlike = models.PostLike(post = post, user = request.user)
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
 ##돌면서 post_id에 얼마나 많은 user_id의 수가 매칭되었는지 저장을 해야되는데.. 그래서.

class PostScore(View):
  def get(self, request, postId):
    LikeJSON = []
    likeList = models.PostScore.objects.filter(post__pk = postId)
    for like in likeList:
      LikeJSON.append(model_to_dict(like))
    likeList = json.dumps(LikeJSON)
    return JsonResponse(likeList, safe=False)

<<<<<<< HEAD
  def post(self, request, postId, score):
=======
  def post(self, request, postId):
    score = request.POST.get('score', 1)
>>>>>>> 8659dcc1ba111575c0a29c41d4e969f31c58ebff
    newlike = models.PostScore(post__pk = postId, user = request.user, score=int(score))
    newlike.save()
    return JsonResponse({'error':0})
  
  def delete(self, request, postId):
    try:
      like = models.PostScore.objects.get(post__pk = postId, user = request.user)
      like.delete()
      return JsonResponse({'error':0})
    except Exception as e:
      print(e)
      return JsonResponse({'error':1})