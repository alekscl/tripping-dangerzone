from django.conf.urls import patterns, url
from blog import views


urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<year>\d{4})/(?P<id>\d+)/$',
        views.blog_entry, name='blog_entry'),
    url(r'^newpost/$', views.new_post, name="new_post"),
)
