from django.shortcuts import render
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from Makini.settings import EMAIL_HOST_USER  



# Create your views here.
def Home(request):
    return render(request, 'index.html', {'nav':'index'})


def about(request):
    return render(request, 'about.html', {'nav':'about'})

def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        # send an email

        send_mail(
            message_name,# subject
            message, # message
            message_email, #email
            ['ngigipaul912@gmail.com'], # To email
        )

        contact = {
            'nav':'contact',
            'message_name':message_name
        }
        return render(request, 'contact.html', context)
    else:
        return render(request, 'contact.html', {'nav':'contact'})


def event(request):
    return render(request, 'events.html', {'nav':'events'})

def course(request):
    return render(request, 'courses.html', {'nav':'courses'})

def trainer(request):
    return render(request, 'trainers.html', {'nav':'trainers'})

def pricing(request):
    return render(request, 'pricing.html', {'nav':'pricing'})