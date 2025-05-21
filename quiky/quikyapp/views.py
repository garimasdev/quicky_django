from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings



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

        message = f"""
        New Booking Inquiry:
        Name: {name}
        Email: {email}
        Phone: {phone}
        Category: {category}
        """

        send_mail(
            subject="New Booking Inquiry",
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=["your-email@example.com"],  # replace with your email
        )

        return redirect('Your message has been sent. Will contact you shortly!')
    return redirect('home')



