from django.urls import path
from . import views

urlpatterns = [
    path('show/', views.home),
    path('list/', views.Post.as_view())
]