from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.forms.models import model_to_dict
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.views import View
from post import models

import json

class LikeView(View):
    def get(self, request):
        LikeJSON = []
        likeList = models.PostLike.objects.filter(user = request.user)
        for like in likeList:
            LikeJSON.append(model_to_dict(like))
            likeList = json.dumps(LikeJSON)
            return JsonResponse(likeList, safe=False)

class signupnew(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'accounts/signup.html', {'form': form},)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(settings.LOGIN_URL) 

def signupold(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(settings.LOGIN_URL)
    else:
        form = UserCreationForm()
        return render(request, 'accounts/signup.html', {'form': form},) 

    # 내가 작성했지만 잘 이해가 안감..조건문의 순서
    pass


# Create your views here.
