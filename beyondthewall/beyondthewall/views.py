from django.views.generic import TemplateView, View

from contact.forms import BeyondContactForm


class TextPlainView(TemplateView):
    content_type = "text/plain; charset=utf-8"


class VCardTemplateView(TemplateView):
    content_type = 'text/x-vcard; charset=utf-8'
    
    def get(self, request, *args, **kwargs):
        response = super(VCardTemplateView, self).get(request, *args, **kwargs)
        response['Content-Disposition'] = 'attachment; filename="%s"' % request.path.split('/')[-1]
        return response


class HomepageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomepageView, self).get_context_data(**kwargs)
        context['form'] = BeyondContactForm(request=self.request)
        return context