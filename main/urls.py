from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'main.views.index', name='index'),
    url(r'^upload/', 'main.views.upload')
)
