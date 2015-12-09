from django.test import SimpleTestCase, Client
from django.core import mail
from django.core.urlresolvers import reverse
# Create your tests here.


class TestSendMailView(SimpleTestCase):


    def setUp(self):
        
        self.client = Client()

        self.url = reverse('send_mail')


    def test_send_email(self):
        response = self.client.post(self.url, {'name': 'Test Name',
            'category': 'Test Category', 'subject': 'Test Subject',
            'message': 'Test Message', 'captcha': 'test cap'}, HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        self.assertEqual(len(mail.outbox), 1)

        self.assertEqual(mail.outbox[0].subject, 'test message')


    def test_redirect(self):
        
        response = self.client.post(self.url, {'name': 'Test Name',
            'category': 'Test Category', 'subject': 'Test Subject',
            'message': 'Test Message', 'captcha': 'test cap'}, HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        self.assertRedirects(response, reverse('home'), status_code=302, 
        	target_status_code=200, msg_prefix='', fetch_redirect_response=True)
    
        

