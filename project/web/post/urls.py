from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('show/', views.home),
    path('detail/<Id>', views.PostDetail),
    path('list/', views.Post.as_view()),
    path('like/<postId>', csrf_exempt(views.PostLike.as_view())),
    path('score/<postId>', csrf_exempt(views.PostScore.as_view())),
]