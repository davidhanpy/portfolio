from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.ShowList),
    path('detail/<int:pk>', views.ShowDetail)
]
