from django.shortcuts import render, HttpResponse
from Home.models import Contact
from django.core.mail import send_mail
# Create your views here.

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = Contact(name=name, subject=subject, email=email, message=message)
        contact.save()
        message_body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

        send_mail(
            subject,
            message_body,
            email,
            ['shethkathan4@gmail.com']
        )
    return render(request, 'index.html')