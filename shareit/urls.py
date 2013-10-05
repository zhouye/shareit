from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from shareit.admin import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'main.views.index', name = "index"),
    url(r'^upload/', 'main.views.upload', name = "upload"),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
