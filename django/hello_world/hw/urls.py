from django.conf.urls import patterns, url
from hw import views

urlpatterns = patterns(
    '',
    url(r'^hello/$', views.hello_view, name='hello_view'),
    url(r'^better/$', views.better_hello, name='better_hello'),
)
