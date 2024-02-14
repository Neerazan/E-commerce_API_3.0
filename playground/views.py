from django.shortcuts import render
from .tasks import notify_customers
# from django.core.mail import EmailMessage, send_mail, mail_admins, BadHeaderError
# from templated_mail.mail import BaseEmailMessage


def say_hello(request):
    # try:
        # send_mail('This is Subject', 'This is Message', 'from@nirajan.com', ['bob@nirajan.com'])

        #Send mail to admin
        # mail_admins('subject', 'message', html_message='message')

        # 
        
        #Templated Mail
    #     message = BaseEmailMessage(
    #         template_name='emails/hello.html',
    #         context={
    #             'name': 'Nirajan'
    #         }
    #     )
    #     message.send(['nirajandhakal@gmail.com'])
    # except:
    #     pass

    # Code for celery
    notify_customers.delay('This is test message..')

    return render(request, 'hello.html', {'name': 'Mosh'})
