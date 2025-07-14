from django.urls import path, include
from Home import views

urlpatterns = [
    path('', views.index, name="index"),
    path('blog/blogpost/<slug:slug>/', views.blogpost, name="blogpost"),
    path('search', views.search, name="search"),
    path('signup', views.handleSignup, name="handleSignup"),
]