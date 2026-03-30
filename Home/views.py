from django.shortcuts import render, HttpResponse
from .models import Post
from .models import Category
from django.db.models import Q
# Create your views here.
def home(request):
   posts = Post.objects.filter(status='published').order_by('-created_at')
   categories = Category.objects.all()

   #auto select featured posts 
   featured_posts = posts[:3] 
   latest_posts = posts[3:]
   return render(request, 'home.html', {'posts':posts,'featured_posts':featured_posts,'latest_posts':latest_posts, 'categories':categories,})

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'post_detail.html', {'post':post})

def category_posts(request, slug):
    category = Category.objects.get(slug=slug)
    posts = Post.objects.filter(category=category, status='published')

    return render(request, 'category.html', {'category':category, 'posts':posts})

def search(request):
    query = request.GET.get('query')

    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query),
            status='published'
        )
    else:
        posts = Post.objects.none()

    return render(request, 'search.html', {
        'posts': posts,
        'query': query
    })