from django.shortcuts import render, HttpResponse
from Home.models import Contact
from django.contrib import messages
# Create your views here.

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = Contact(name=name, subject=subject, email=email, message=message)
        contact.save()
        messages.success(request, "Your message has been successfully sent")
    return render(request, 'index.html')