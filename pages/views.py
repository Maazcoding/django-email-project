from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .forms import ContactForm

def home(request):
    # Render + Template Variables
    context = {'title': 'Home', 'welcome_msg': 'welcome to our django site!'}
    return render(request, 'pages/home.html', context)

def about(request, year=None):
    # Path converter demo: year is captured from URL if provided
    context = {
        'title': 'About Us',
        'year': year or 2024,
        'features': ['fast', 'secure', 'scalable', 'user-friendly']
    }
    return render(request, 'pages/about.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Extract cleaned data
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Send email to admin
            subject = f'New Contact Submission from {name}'
            body = f'Name: {name}\nPhone: {phone}\nEmail: {email}\n\nMessage:\n{message}'
            
            send_mail(
                subject, body,
                settings.DEFAULT_FROM_EMAIL,
                [settings.ADMIN_EMAIL],
                fail_silently=False,
            )
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'pages/contact.html', {'form': form, 'title': 'Contact Us'})

def plain_response(request):
    # HttpResponse example (no template)
    return HttpResponse("This is a raw HttpResponse. No template rendering used.")