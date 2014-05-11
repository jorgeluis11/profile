from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from .views import index
admin.autodiscover()
import os


urlpatterns = patterns('',
    # Examples:
    url(r'^admin', include(admin.site.urls)),      
    url(r'^$', index, name='index'), 
    url(r'^home$', index, name='index'),   

    # (r'^media/(.*)$', 'django.views.static.serve', {'document_root': os.path.join(os.path.dirname(__file__), 'media')}),

)

urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
    'document_root': settings.MEDIA_ROOT}))

urlpatterns += patterns('',
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
     {'document_root': settings.STATICFILES_DIRS[0], 'show_indexes': True}),
)