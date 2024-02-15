from django.core.cache import cache
from django.shortcuts import render
import requests
# from .tasks import notify_customers
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
    # notify_customers.delay('This is test message..')


    #Code for caching
    key = 'httpbin_result'
    if cache.get('httpbin_result') is None:
        response = requests.get('https://httpbin.org/delay/3')
        data = response.json()
        cache.set(key, data)

    return render(request, 'hello.html', {'name': cache.get(key)})
