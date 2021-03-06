from django.core.mail import EmailMessage
from django.conf import settings

from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3
from contact_form.forms import ContactForm


class BeyondContactForm(ContactForm):
    captcha = ReCaptchaField(widget=ReCaptchaV3)

    recipient_list = ['%s <%s>' % mail_tuple for mail_tuple in settings.MANAGERS]
    
    def get_message_dict(self):
        if not self.is_valid():
            raise ValueError("Message cannot be sent from invalid contact form")
        return {
                'to': self.recipient_list,
                'from_email': self.from_email,
                'subject': self.subject(),
                'body': self.message(),
                'headers': {'Reply-To': '%s <%s>' % (self.data['name'], self.data['email'])}
                }
    
    
    def save(self, fail_silently=False):
        message_dict = self.get_message_dict()
        mail = EmailMessage(**message_dict)
        mail.send(fail_silently)