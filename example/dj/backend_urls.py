from django.conf.urls import patterns, url

from test_chamber import views

urlpatterns = patterns(
    '',
    url(r'^current_time_backend/$', views.current_datetime, name='current-datetime')
)