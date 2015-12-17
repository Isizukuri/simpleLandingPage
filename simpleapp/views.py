from django.views.generic.edit import FormView
from django.core.mail import send_mail

from sendmail.settings import ADMIN_EMAIL
from simpleapp.forms import FeedbackForm

# Create your views here.


class MainPage(FormView):
    template_name = 'home.html'
    form_class = FeedbackForm

    def form_valid(self, form):
        name = 'Full name: ' + form.cleaned_data.get('name') + '\n'
        category = 'Category: ' + form.cleaned_data.get('category') + '\n'
        subject = 'Subject: ' + form.cleaned_data.get('subject') + '\n'
        text = 'Text: ' + form.cleaned_data.get('text') + '\n'
        message = name + category + subject + text
        send_mail('Feedback from ' + form.cleaned_data.get('name'),
                  message, 'test@mail.com',
                  [ADMIN_EMAIL])
        print form.cleaned_data
        form.save()
        return super(MainPage, self).form_valid(form)
