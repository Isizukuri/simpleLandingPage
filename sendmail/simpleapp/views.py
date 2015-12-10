from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.core.mail import send_mail as sm

from sendmail.settings import ADMIN_EMAIL

from simpleapp.forms import ContactForm

# Create your views here.


class MainPage(FormView):
    template_name = 'home.html'
    form_class = ContactForm

    def post(self, request):
        form = request.POST
        message = u''
        for value in form.values():
            message += (value + u' ')
        sm('test message', message, 'test@mail.com', [ADMIN_EMAIL])
        return HttpResponseRedirect(reverse('home'))

def send_mail(request):
    if request.method == 'POST':
        form = request.POST
        message = u''
        for value in form.values():
            message += (value + u' ')
        sm('test message', message, 'test@mail.com', [ADMIN_EMAIL])
        return HttpResponseRedirect(reverse('home'))
    else:
        return HttpResponse('<p>Incorrect method</p>')
