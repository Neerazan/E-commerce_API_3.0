from django.shortcuts import render
from django.core.mail import EmailMessage, send_mail, mail_admins, BadHeaderError


def say_hello(request):
    try:
        # send_mail('This is Subject', 'This is Message', 'from@nirajan.com', ['bob@nirajan.com'])

        #Send mail to admin
        # mail_admins('subject', 'message', html_message='message')

        message = EmailMessage('attach file', 'Try to attach file in message', 'from@nirajan.com', ['john@nirajan.com'])

        message.attach_file('playground/static/images/mail_test.png')
        message.send()
    except:
        pass

    return render(request, 'hello.html', {'name': 'Mosh'})
