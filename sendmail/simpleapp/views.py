import json
import requests

from django.views.generic.base import TemplateView
from django.http import JsonResponse
from django.core.mail import send_mail as sm

from sendmail.settings import ADMIN_EMAIL

# Create your views here.


class MainPage(TemplateView):
    template_name = 'home.html'


def send_mail(request):

    def get_client_ip(request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    if request.method == 'POST':
        form = json.loads(request.body)
        captcha_rs = form.get('g-recaptcha-response')
        url = "https://www.google.com/recaptcha/api/siteverify"
        params = {
            'secret': u'6Lek2xITAAAAAEWo-jsppfNgdRFEzqIztP9EnHVd',
            'response': unicode(captcha_rs),
            'remoteip': get_client_ip(request)
        }
        verify_rs = requests.get(url, params=params, verify=True)
        verify_rs = verify_rs.json()
        response = {}
        response["status"] = verify_rs.get("success", False)
        if response['status']:
            name = 'Full name: ' + form.get('name') + '\n'
            category = 'Category: ' + form.get('category') + '\n'
            subject = 'Subject: ' + form.get('subject') + '\n'
            text = 'Text: ' + form.get('message') + '\n'
            message = name + category + subject + text
            sm('Feedback from ' + form.get('name'), message, 'test@mail.com',
                [ADMIN_EMAIL])
        else:
            response['message'] = verify_rs.get('error-codes', None)
        return JsonResponse(response)
