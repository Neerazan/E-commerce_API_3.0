from django.shortcuts import render
from django.core.mail import send_mail, mail_admins, BadHeaderError


def say_hello(request):
    try:
        # send_mail('This is Subject', 'This is Message', 'form@nirajan.com', ['bob@nirajan.com'])

        #Send mail to admin
        mail_admins('subject', 'message', html_message='message')
    except:
        pass

    return render(request, 'hello.html', {'name': 'Mosh'})
