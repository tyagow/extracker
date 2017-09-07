from django.conf.urls import url

from src.core import views as core_views


urlpatterns = [
    url(r'^deep/(?P<operation>\w+)/(?P<value>\w+)/$', core_views.deep, name='deep'),
    url(r'^$', core_views.home, name='home'),
]
