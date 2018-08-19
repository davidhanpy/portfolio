from django.urls import path
from . import views

urlpatterns = [
    path('show/', views.home),
    path('detail/<Id>', views.PostDetail),
    path('list/', views.Post.as_view()),
    path('like/<postId>', views.PostLike.as_view()),
    path('score/<postId>/<score>', views.PostScore.as_view())
]