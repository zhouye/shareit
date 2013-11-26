from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

from shareit.admin import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'main.views.index', name = "index"),
    url(r'^upload/', 'main.views.upload', name = "upload"),

    url(r'^file/(?P<file_id>\w+)/$', 'main.views.file', name = "file"),


    url(r'^accounts/', include('registration.backends.simple.urls')),

    url(r'^friendship/', include('friendship.urls')),

    url(r'^comment/', include('django_comments.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
