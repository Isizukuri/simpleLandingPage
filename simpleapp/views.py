from django.views.generic.edit import FormView
from django.core.mail import send_mail

from sendmail.settings import ADMIN_EMAIL
from simpleapp.forms import FeedbackForm

# Create your views here.


class MainPage(FormView):
    template_name = 'home.html'
    form_class = FeedbackForm

    def form_valid(self, form):
        send_mail('Feedback',
                  'Message', 'test@mail.com',
                  [ADMIN_EMAIL])
        form.save()
        return super(MainPage, self).form_valid(form)
