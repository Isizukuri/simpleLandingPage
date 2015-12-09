from django import forms
from captcha.fields import CaptchaField


class ContactForm(forms.Form):
    name = forms.CharField()
    category = forms.CharField()
    subject = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)
    captcha = CaptchaField()
