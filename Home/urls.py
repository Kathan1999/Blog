from django.contrib import admin
from django.urls import path, include
from Home import views

urlpatterns = [
   path('', views.home, name="home"),
   path('post/<slug:slug>/', views.post_detail, name='post_detail')
]