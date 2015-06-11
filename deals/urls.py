from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^create/$', views.add_model, name='create'),
    url(r'^(?P<pk>[0-9]+)/edit/$', views.update_model, name='update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.delete_model, name='delete')
]