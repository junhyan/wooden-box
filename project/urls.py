from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static

from notebook import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index),
    url(r'^health$', views.health),
    url(r'^add_user$', views.add_user),
    url(r'^get_user_by_id/(?P<book_id>\d+)$', views.get_user_by_id),
    url(r'^admin/', include(admin.site.urls)),

    #used for web page render
    url(r'^register/$', register),

    # for static file used in product
    static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
