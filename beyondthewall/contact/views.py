from contact_form.views import ContactFormView

from .forms import BeyondContactForm

class BeyondContactFormView(ContactFormView):
    form_class = BeyondContactForm