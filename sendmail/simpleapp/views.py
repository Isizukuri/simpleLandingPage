import json

from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.core.mail import send_mail as sm

from sendmail.settings import ADMIN_EMAIL

from simpleapp.forms import ContactForm

# Create your views here.


class MainPage(TemplateView):
    template_name = 'home.html'
    
    def post(self, request):
        form = json.loads(request.body)
        sm('test message', unicode(form), 'test@mail.com', [ADMIN_EMAIL])
        return HttpResponseRedirect(reverse('home'))

def send_mail(request):
    if request.method == 'POST':
        form = json.loads(request.body)
        sm('test message', unicode(form), 'test@mail.com', [ADMIN_EMAIL])
        return HttpResponseRedirect(reverse('home'))
    else:
        return HttpResponse('<p>Incorrect method</p>')
