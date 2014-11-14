from django.conf.urls import patterns, include, url
from guitar_app import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^guitar_detail/(?P<pk>[a-z\d]+)/', views.guitar_detail, name='guitar_detail'),
    url(r'^action/', views.action, name='action'),
    url(r'^add/', views.add, name='add'),
    url(r'^statistics/', views.statistics, name='statistics'),
)
