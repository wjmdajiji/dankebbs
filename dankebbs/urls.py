from django.conf.urls import patterns, include, url
import login.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dankebbs.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', login.views.welcome),
)
