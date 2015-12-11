import json
import requests

from django.views.generic.base import TemplateView
from django.http import JsonResponse
from django.core.urlresolvers import reverse
from django.core.mail import send_mail as sm

from sendmail.settings import ADMIN_EMAIL

# Create your views here.


class MainPage(TemplateView):
    template_name = 'home.html'

    def post(self, request):
        form = json.loads(request.body)
        sm('test message', unicode(form), 'test@mail.com', [ADMIN_EMAIL])
        return HttpResponseRedirect(reverse('home'))


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
        response['message'] = verify_rs.get(
            'error-codes', None) or "Unspecified error."
        if response['status']:
            sm('test message', unicode(form), 'test@mail.com', [ADMIN_EMAIL])
        return JsonResponse(response)
        
