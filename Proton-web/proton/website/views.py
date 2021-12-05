from django.shortcuts import render
from django.core.mail import send_mail
from proton import settings
from django.contrib import messages

# Create your views here.

def home(request):
    if request.method == 'POST':
        user_name = request.POST.get('name')
        user_email = request.POST.get('email')
        message = request.POST.get('message')

        #send mail to me
        send_mail(
            f'THE PROTON GUY - Contact Form Entry - {user_name}', #subject
            message, #message to be sent
            user_email, #from email
            ['theprotonguy1@gmail.com'], #to email
            # fail_silently=True
        )

        #send email to user
        send_mail(
            'THE PROTON GUY - Contact Form Entry',
            f'Hello {user_name}. Thank you for visiting our website and contacting us. This is a verification email to confirm your request below: {message}.We will be in touch with you shortly!',
            settings.EMAIL_HOST_USER,
            [user_email],
            # fail_silently=True
        )
        # subject = ''
        # message = f'Hello {name}. Thank you for visiting our website and contacting us. This is a verification email to confirm your request below: {message}.We will be in touch with you shortly!'
        # from_email = settings.EMAIL_HOST_USER
        # to_list = [user_email, 'theprotonguy1@gmail.com']
        # send_mail(subject, message, from_email, to_list, fail_silently=True)

        #confirmation
        messages.success(request, 'Your request has been received! We will reply shortly...')

        return render(request, 'website/index.html', {'name': user_name})

    return render(request, 'website/index.html', {})

