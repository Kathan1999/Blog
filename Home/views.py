from django.shortcuts import render, HttpResponse
from .models import Post
from .models import Category
from django.db.models import Q
from django.core.paginator import Paginator
# Create your views here.
def home(request):
   all_posts = Post.objects.filter(status='published').order_by('-created_at')
   featured_posts = all_posts[:3]
   remaining_posts = all_posts[3:]
   paginator = Paginator(remaining_posts, 6)
   page_number = request.GET.get('page')
   posts = paginator.get_page(page_number)

   catogories = Category.objects.all()

   return render(request, 'home.html', {'featured_posts':featured_posts, 'posts':posts, 'categories':catogories,})

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