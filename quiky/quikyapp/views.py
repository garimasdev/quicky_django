from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings

import ssl
import certifi

# Ensure Python uses the certificates provided by certifi
ssl_context = ssl.create_default_context(cafile=certifi.where())
ssl._create_default_https_context = ssl_context


def home(request):
    return render(request, 'index.html')


def contact_us(request):
    return render(request, 'contact.html')


def blog(request):
    return render(request, 'blog.html')



def contact_submit(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        category = request.POST.get("category")
        message = request.POST.get('message')

        message = f"""
        New Booking Inquiry:
        Name: {name}
        Email: {email}
        Phone: {phone}
        Category: {category}
        Message: {message}
        """

        send_mail(
            subject=f"New Booking Inquiry from quiky {name}",
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=["support@quikymeals.com"],  # replace with your email
        )

        return redirect('Your message has been sent. Will contact you shortly!')
    return redirect('contact')



