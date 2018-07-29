from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [\
  path('login/', auth_views.login, {'template_name': 'login.html'}, name='login'),
  path('logout/', auth_views.logout, name='logout'),
  path('regist/', auth_views.regist, name='regist')
]
