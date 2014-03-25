"Tests forms of contact app."
from django.core import mail
from django.test import RequestFactory
from django.test import TestCase
from django.conf import settings

import contact_form.tests.forms

from .forms import BeyondContactForm

class ContactFormsTests(contact_form.tests.forms.ContactFormTests):
    """Tests stuff not covered by contact_form app
    see https://bitbucket.org/ubernostrum/django-contact-form"""
    
    def test_send(self):
        "Test sending of emails. form.email should be in reply-to header field."
        request = RequestFactory().request()
        data = {'name': 'Test',
                'email': 'test@example.com',
                'body': 'Test message'}
        form = BeyondContactForm(request=request, data=data)
        form.recipient_list = ['recipient@example.com']
        self.assertTrue(form.is_valid())
        form.save()
        
        self.assertEqual(1, len(mail.outbox))
        message = mail.outbox[0]
        
        self.assertEqual(form.recipient_list, message.recipients())
        self.assertIn('Reply-To', message.extra_headers)
        self.assertIn(data['email'], message.extra_headers['Reply-To'])
        self.assertTrue(data['body'] in message.body)
        self.assertEqual(settings.DEFAULT_FROM_EMAIL,
                          message.from_email)
    
    def test_default_recipients(self):
        "Mail recipients are managers"
        request = RequestFactory().request()
        form = BeyondContactForm(request=request, data={})
        
        self.assertEqual(['%s <%s>' % (name, email) for (name, email) in settings.MANAGERS],
                         form.recipient_list)
        