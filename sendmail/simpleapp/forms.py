from django import forms


class ContactForm(forms.Form):
    name = forms.CharField()
    category = forms.CharField()
    subject = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)
    captcha = forms.CharField(required=False)
