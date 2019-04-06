from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = "connection"

urlpatterns = [
    # /connection/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # /connection/71/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # /connection/new
    url(r'^new/$', views.ConnectionCreate.as_view(), name='create'),
    # connection/update/2/
    url(r'^update/(?P<pk>[0-9]+)/$', views.ConnectionUpdate.as_view(), name="update"),
    # /connection/delete
    url(r'(?P<pk>[0-9]+)/delete/$', views.ConnectionDelete.as_view(), name="delete"),
    # /connection/2/query/
    url(r'^(?P<pk>[0-9]+)/query$', views.DBQuery.as_view(), name="query"),
    # url(r'^query/(?P<pk>[0-9]+)/$', views.DBQuery.as_view(), name="query"),

]

urlpatterns = format_suffix_patterns(urlpatterns)