from django.shortcuts import render, HttpResponse
from .models import Post
# Create your views here.
def home(request):
   posts = Post.objects.filter(status='published').order_by('-created_at')
   return render(request, 'home.html', {'posts':posts})

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'post_detail.html', {'post':post})