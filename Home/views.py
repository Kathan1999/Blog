from django.shortcuts import render, HttpResponse
from Home.models import Contact
from django.contrib import messages
from Home.models import LeftPost
from Home.models import RightPost
# Create your views here.

def index(request):
    allLeftPosts = LeftPost.objects.all()
    allRightPosts = RightPost.objects.all()
    context = {'allLeftPosts':allLeftPosts, 'allRightPosts':allRightPosts}
    if request.method == 'POST':
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = Contact(name=name, subject=subject, email=email, message=message)
        contact.save()
        messages.success(request, "Your message has been successfully sent")
    return render(request, 'index.html', context)

def blogpost(request):
    return render(request, 'blogpost.html')