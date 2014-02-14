from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView, RedirectView
from django.conf import settings
from django.http import HttpResponse

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

class TextPlainView(TemplateView):
    def render_to_response(self, context, **kwargs):
        mimetype = 'text/plain; charset=utf-8'
        return super(TextPlainView, self).render_to_response(context, 
                                                             content_type=mimetype,
                                                             **kwargs)



urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='home.html')),
    url(r'^contact/', include('contact.urls')),
    
    url(r'^robots\.txt$', TextPlainView.as_view(template_name='robots.txt')),
    url(r'^humans\.txt$', TextPlainView.as_view(template_name='humans.txt')),
    url(r'^favicon\.ico$', RedirectView.as_view(url=settings.STATIC_URL + 'img/favicon.ico')),
    (r'^google7f92da28d3dd66e7\.html$', lambda r: HttpResponse("google-site-verification: google7f92da28d3dd66e7.html", mimetype="text/plain")),

    # Examples:
    # url(r'^$', 'beyondthewall_project.views.home', name='home'),
    # url(r'^beyondthewall_project/', include('beyondthewall_project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
)
