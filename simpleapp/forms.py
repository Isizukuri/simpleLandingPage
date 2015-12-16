from django.forms import ModelForm
from simpleapp.models import Feedback


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'category', 'subject', 'text']
