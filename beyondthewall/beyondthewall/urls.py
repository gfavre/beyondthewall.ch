from django.conf.urls import include, url
from django.views.generic import RedirectView, TemplateView
from django.conf import settings
from django.http import HttpResponse

from .views import TextPlainView, VCardTemplateView, HomepageView

urlpatterns = [
    url(r'^$', HomepageView.as_view()),
    url(r'^contact/', include('contact.urls')),
    url(r'^vcard-Gregory-Favre\.vcf$',
        VCardTemplateView.as_view(template_name='vcard.vcf'),
        name='vcard'),

    url(r'^robots\.txt$', TextPlainView.as_view(template_name='robots.txt')),
    url(r'^humans\.txt$', TextPlainView.as_view(template_name='humans.txt')),
    url(r'^favicon\.ico$', RedirectView.as_view(url=settings.STATIC_URL + 'img/favicon.ico')),
    url(r'^google7f92da28d3dd66e7\.html$',
        lambda r: HttpResponse("google-site-verification: google7f92da28d3dd66e7.html", mimetype="text/plain")),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
