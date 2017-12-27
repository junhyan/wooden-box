from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.views.static import serve

from notebook import views
from notebook import api 
from notebook import upload 

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # api
    url(r'^add_user$', api.add_user),
    url(r'^get_user_by_id/(?P<id>\d+)$', api.get_user_by_id),
    url(r'^upload/(?P<dir_name>[^/]+)$', upload.upload_image),
    url(r'^upload/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }),



    #used for web page render
    url(r'^$', views.index),
    url(r'^editor$', views.editor),
    url(r'^register/$', views.register),
    url(r'^health$', views.health),
    url(r'^admin/', include(admin.site.urls)),

    # for static file used in product
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
