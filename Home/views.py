from django.shortcuts import render, HttpResponse, redirect
from django.shortcuts import get_object_or_404
from Home.models import Contact
from django.contrib import messages
from Home.models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
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

def search(request):
    query = request.GET.get('query','')
    allPosts = Post.objects.filter(title__icontains=query)
    params = {'allPosts':allPosts, 'query':query}
    return render(request, 'blog/search.html', params)

def handleSignup(request):
    if request.method == 'POST':
        #Get the post parameters
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        #check for errorneous inputs
        if len(username) > 10:
            messages.error(request, "Username must be under 10 characters")
            return redirect('/')
        
        if not username.isalnum():
            messages.error(request, "Username should only contain letters and numbers")
            return redirect('/')

        if pass1 != pass2:
            messages.error(request, 'password do not match')
            return redirect('/')
        
        #Create the User
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your blog account has been successfully created")
        return redirect('/')
    else:
        return HttpResponse('404 - Not Found')
    
def handleLogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpass = request.POST['loginpass']

        user = authenticate(username=loginusername, password=loginpass)

        if user is not None:
            login(request, user)
            messages.success(request, "successfully logged in")
            return redirect('/')
        else:
            messages.success(request, "Invalid Credentials, Please try again")
            return redirect('/')
    return HttpResponse("hello")


def handleLogout(request):
        logout(request)
        messages.success(request, "Successfully Logged out")
        return redirect("/")
    