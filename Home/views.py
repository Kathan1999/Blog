from django.shortcuts import render, HttpResponse
from django.shortcuts import get_object_or_404
from Home.models import Contact
from django.contrib import messages
from Home.models import Post
# Create your views here.

def index(request):
    allPosts = Post.objects.all()
    context = {'allPosts':allPosts}
    if request.method == 'POST':
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = Contact(name=name, subject=subject, email=email, message=message)
        contact.save()
        messages.success(request, "Your message has been successfully sent")
    return render(request, 'blog/index.html', context)

def blogpost(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/blogpost.html', {'post':post})