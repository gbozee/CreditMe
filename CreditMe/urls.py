from django.conf.urls import patterns, include, url
from api.handlers import *
from tastypie.api import Api
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

oncredit_api = Api(api_name='oncredit')
oncredit_api.register(PrepaidResource())
oncredit_api.register(CableTVResource())
oncredit_api.register(CableSubscriptionResource())
oncredit_api.register(PostpaidResource())
oncredit_api.register(UserResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CreditMe.views.home', name='home'),
    # url(r'^CreditMe/', include('CreditMe.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^api/', include('api.urls')),
    url(r'^api/', include(oncredit_api.urls)),
)
