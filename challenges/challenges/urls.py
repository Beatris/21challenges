from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'challenges.views.home', name='home'),
    # url(r'^challenges/', include('challenges.foo.urls')),

    url(r'^accounts/', include('registration.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
