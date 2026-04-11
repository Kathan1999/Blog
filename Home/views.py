from django.shortcuts import render, HttpResponse
from .models import Post
from .models import Category
from django.db.models import Q
from django.core.paginator import Paginator
from django.conf import settings
from django.utils.text import slugify
# Create your views here.
def home(request):
   all_posts = Post.objects.filter(status='published').order_by('-created_at')
   featured_posts = all_posts[:3]
   remaining_posts = all_posts[3:]
   trending_posts = Post.objects.filter(status='published').order_by('-views')[:5]
   paginator = Paginator(remaining_posts, 6)
   page_number = request.GET.get('page')
   posts = paginator.get_page(page_number)

   catogories = Category.objects.all()

   return render(request, 'home.html', {'featured_posts':featured_posts, 'posts':posts, 'categories':catogories,'trending_posts':trending_posts})

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)

    post.views += 1
    post.save()
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


def generate_blog(request):
    content = None
    topic = request.GET.get('topic')

    if topic:
        content = f"""
{topic}

This is a generated blog about {topic}.

Top Picks:
1. Product A
2. Product B
3. Product C

Buying Guide:
- Check features
- Compare prices

Conclusion:
Best options for {topic}.
        """

        title = topic

        # 🔥 SLUG LOGIC
        base_slug = slugify(title)
        slug = base_slug
        counter = 1

        while Post.objects.filter(slug=slug).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1

        # 🔥 SMART CATEGORY DETECTION
        topic_lower = topic.lower()

        if any(word in topic_lower for word in ['earbud', 'phone', 'laptop', 'tablet']):
            category = Category.objects.filter(name__icontains='electronics').first()

        elif any(word in topic_lower for word in ['shoe', 'shirt', 'jeans', 'fashion']):
            category = Category.objects.filter(name__icontains='fashion').first()

        elif any(word in topic_lower for word in ['gym', 'fitness', 'protein']):
            category = Category.objects.filter(name__icontains='fitness').first()

        else:
            category = Category.objects.first()

        # 🚀 CREATE POST
        Post.objects.create(
            title=title,
            slug=slug,
            content=content,
            excerpt=content[:150],
            author="AI Generator",
            status='published',
            category=category
        )

    return render(request, 'ai_generate.html', {
        'content': content,
        'topic': topic
    })