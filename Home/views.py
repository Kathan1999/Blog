from django.shortcuts import render, HttpResponse
from .models import Post
# Create your views here.
def home(request):
   posts = Post.objects.filter(status='published').order_by('-created_at')

   #auto select featured posts 
   featured_posts = posts[:3] 
   latest_posts = posts[3:]
   return render(request, 'home.html', {'posts':posts,'featured_posts':featured_posts,'latest_posts':latest_posts})

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'post_detail.html', {'post':post})