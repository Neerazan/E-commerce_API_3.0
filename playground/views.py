from django.core.cache import cache
from django.views.decorators.cache import cache_page
from rest_framework.views import APIView
from django.shortcuts import render
from django.utils.decorators import method_decorator
import requests
# from .tasks import notify_customers
# from django.core.mail import EmailMessage, send_mail, mail_admins, BadHeaderError
# from templated_mail.mail import BaseEmailMessage

# @cache_page(5*60)
# def say_hello(request):
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
    # response = requests.get('https://httpbin.org/delay/3')
    # data = response.json()

    # return render(request, 'hello.html', {'name': data})



#Cache in Class Base view
class HelloView(APIView):
    @method_decorator(cache_page(5*60))
    def get(self, request):
        response = requests.get('https://httpbin.org/delay/3')
        data = response.json()
        return render(request, 'hello.html', {'name': data})