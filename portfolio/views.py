from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact


def home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Save to database
        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        
        messages.success(request, 'Your message has been sent successfully! I will get back to you soon.')
        return redirect('contact')
        
    return render(request, "contact.html")